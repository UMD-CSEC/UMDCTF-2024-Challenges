use std::net::Ipv4Addr;
use std::time::Duration;
use bytes::Bytes;
use http_body_util::Empty;
use hyper::body::Incoming;
use hyper::{Request, Response, StatusCode};
use hyper::service::service_fn;
use hyper_util::rt::TokioIo;
use tokio::net::{TcpListener, TcpStream};
use tokio::io::{AsyncReadExt, AsyncWriteExt};

#[tokio::main]
async fn main() {
    let listener = TcpListener::bind((Ipv4Addr::from(0), 8888)).await
        .unwrap();

    let (stream, _) = listener.accept().await.unwrap();

    let _ = hyper::server::conn::http1::Builder::new()
        .serve_connection(TokioIo::new(stream), service_fn(first_connection))
        .with_upgrades()
        .await;

    let (stream, _) = listener.accept().await.unwrap();

    let _ = hyper::server::conn::http1::Builder::new()
        .serve_connection(TokioIo::new(stream), service_fn(second_connection))
        .with_upgrades()
        .await;

    tokio::time::sleep(Duration::from_secs(1000)).await;
}

async fn first_connection(request: Request<Incoming>) -> Result<Response<Empty<Bytes>>, anyhow::Error> {
    tokio::spawn(async move {
        first_connection_inner(request).await;
    });

    Ok(Response::builder().status(StatusCode::OK).body(Empty::<Bytes>::new()).unwrap())
}

async fn first_connection_inner(request: Request<Incoming>) -> Result<(), anyhow::Error> {
    let mut incoming_stream = TokioIo::new(hyper::upgrade::on(request).await?);
    let mut outgoing_stream = TcpStream::connect("challs.umdctf.io:31111").await?;

    let mut buf = [0; 8192];
    let bytes_read = incoming_stream.read(&mut buf).await?;
    outgoing_stream.write_all(&buf[0..bytes_read]).await?;

    let bytes_read = outgoing_stream.read(&mut buf).await?;
    incoming_stream.write_all(&buf[0..bytes_read]).await?;

    incoming_stream.read_exact(&mut buf[0..80]).await?;
    outgoing_stream.write_all(&buf[0..80]).await?;

    loop {
        if let Ok(Ok(_)) = tokio::time::timeout(Duration::from_secs(1), async {
            let bytes_read = outgoing_stream.read(&mut buf).await?;
            incoming_stream.write_all(&buf[0..bytes_read]).await?;
            return Ok::<(), anyhow::Error>(());
        }).await {
            continue;
        }

        break;
    }

    incoming_stream.shutdown().await?;
    outgoing_stream.shutdown().await?;

    Ok(())
}

async fn second_connection(request: Request<Incoming>) -> Result<Response<Empty<Bytes>>, anyhow::Error> {
    tokio::spawn(async move {
        second_connection_inner(request).await;
    });

    Ok(Response::builder().status(StatusCode::OK).body(Empty::<Bytes>::new()).unwrap())
}

async fn second_connection_inner(request: Request<Incoming>) -> Result<(), anyhow::Error> {
    let mut incoming_stream = TokioIo::new(hyper::upgrade::on(request).await?);

    let mut buf = [0; 8192];
    let bytes_read = incoming_stream.read(&mut buf).await?;

    for _ in 0..20 {
        let mut outgoing_stream = TcpStream::connect("challs.umdctf.io:31111").await?;
        outgoing_stream.write_all(&buf[0..bytes_read]).await?;
        tokio::time::sleep(Duration::from_secs(1)).await;
    }

    incoming_stream.shutdown().await?;

    Ok(())
}



