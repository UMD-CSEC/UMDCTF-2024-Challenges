
from pwn import *
io = process("./reality")
b = [b"-0.22141951590424758",b"0.21966948131283365",b"0.2668465299942324",b"0.3683726211409554",b"0.04049629904901489",b"-0.3270265646585122",b"-0.13622634211946427",b"-0.057353955546073365",b"-0.15197715314439678",b"-0.4212176178516551",b"-0.17447822845349872",b"-0.11903508235063512",b"-0.5219155197294406",b"0.19436194371798454",b"0.10036995091129526",b"-0.0196552130871671",b"-0.29637993627207837",b"-0.2578161197555048",b"0.060320537614757266",b"-0.0503483501366643",b"0.3137968920954991",b"-0.21670858472591187",b"-0.23295232142975011",b"-0.0568959987176322",b"-0.5878768087915457",b"0.4160774432555711",b"0.13850102127435363",b"-0.029685624671052874",b"0.08521167820929666",b"-0.3002507475856591",b"-0.12247424690793039",b"0.3517119551497332",b"-0.07854620078402336",b"-0.030021643681541144",b"-0.4177128563827017",b"-0.057433563221676594",b"0.3154165822644265",b"-0.1713686777647612",b"-0.24358494043921852",b"0.0858231361525689",b"0.1461725743179145",b"0.6220838182344335",b"-0.18736798237787225",b"-0.1910518031044051",b"-0.03047919708090233",b"-0.40021783091553587",b"0.1913343841082964",b"0.0010690104092457992",b"0.05238717064345995",b"0.5041013830379499",b"-0.12076184364509528",b"0.11565615335206272",b"-0.5409895449425168",b"0.3192098151141187",b"0.1233493259111059",b"0.03296673567784214",b"0.05258864706889882",b"0.14575035463799832",b"-0.041979184290606",b"-0.28592983495383256",b"-0.29964472226965433",b"0.012822131550409434",b"0.47297282054071155",b"-0.38571624127710213",b"-0.1550541112136525",b"0.44065482417539614",b"0.2268735920427214",b"0.0859115545516279",b"0.33615575581943763",b"-0.2803544216410845",b"-0.13015474629004406",b"-0.07043125190588735",b"-0.12857490390504508",b"-0.1738810178300324",b"0.015206076128452133",b"-0.15273185236022344",b"0.08888242427249897",b"-0.01003928564676821",b"-0.13851511191326468",b"-0.2424770997519246",b"-0.06475333068251732",b"-0.0770784853529044",b"-0.027581531370696057",b"-0.28752759108338294",b"0.23708944790846073",b"0.20960046792083295",b"-0.585689541804109",b"-0.19500703343752993",b"-0.2691070108622423",b"-0.49345846539437765",b"-0.4171595859459878",b"0.14301985343151608",b"-0.2808312418871698",b"0.2139528323290792",b"-0.33118907775827483",b"-0.10150982769116186",b"0.04433343840405284",b"0.08283555288968367",b"0.2773038544870713",b"-0.08024358852915801",b"0.34338487221895253",b"-0.28056708024531357",b"0.2748233283924706",b"-0.014589885909776737",b"0.44311998687662113",b"-0.008109905568777494",b"0.08959035665283628",b"0.329863654534821",b"-0.03800308658782319",b"0.29670581916688843",b"0.2777340001526247",b"-0.2589784249994368",b"-0.21775290236347639",b"-0.38715639734705437",b"0.13688334097347246",b"0.3855942704734995",b"-0.017848449849072107",b"0.011913161166278292",b"-0.22104079917953795",b"0.48514664921476763",b"-0.43394082757914815",b"-0.15670994276501893",b"-0.007831861242770605",b"0.05997393113842289",b"-0.2476047187870753",b"0.1352101167636247",b"-0.6614707810235374",b"-0.024413509319586076",b"0.00990795142789179",b"0.26528366776719303",b"-0.3608015904242704",b"0.24383052073807526",b"0.062323105866111256",b"-0.016499424237230415",b"-0.038581765112367626",b"-0.31509772505136274",b"-0.2982049329601135",b"-0.42424630261863766",b"-0.19566101219096516",b"0.2373281507499572",b"-0.05620136685439338",b"0.24137945220343998",b"-0.0038983403423722574",b"-0.3858475684452608",b"-0.19687768270853587",b"-0.3553974469421546",b"-0.06754131609649335",b"-0.03281950479649638",b"-0.33211928768513316",b"0.21416796918764355",b"0.09511527269250754",b"-0.16265154799590617",b"0.3263467220161577",b"0.142175749924114",b"-0.030457340903102672",b"-0.44304504670164596",b"-0.12708356396535028",b"0.13168742147558235",b"0.06579518289077545",b"-0.25855595093701633",b"0.06283548329437437",b"0.14841142481394962",b"0.33219324161462616",b"-0.6196119852911713",b"-0.12508901969236008",b"0.32717233758078806",b"-0.04808190028990016",b"0.04446674507990679",b"0.19550310083890451",b"-0.3662599685117",b"0.12000391682802368",b"0.08838094192418405",b"-0.6699426001863162",b"-0.0015973793797571106",b"-0.059707215561604965",b"-0.3544908363692532",b"-0.2468040705675735",b"0.15683936464889764",b"-0.11070794003389908",b"0.13515811364184177",b"0.21174845402011067",b"0.6483331076741726",b"-0.28644506723544433",b"-0.3899810204560538",b"0.07034151944640335",b"-0.011223883649217642",b"-0.3817094861077248",b"0.011863695564838761",b"0.07299699587592874",b"-0.2925440287105438",b"-0.1655709913123296",b"-0.03891857832573464",b"0.10380641853687914",b"-0.1371161514038292",b"0.018932150577775933",b"0.057855283253097856",b"0.23853376324262077",b"-0.15706091310570092",b"0.6196266145469445",b"0.16850065921813512",b"0.49531297655071505",b"0.0836464058079546",b"0.2742661335905259",b"0.04838995473205361",b"0.04200265997171913",b"-0.13052759457830873",b"-0.01767501084081118",b"-0.07689046177597574",b"-0.35875363181814834",b"-0.13831524284628277",b"0.19064740984904355",b"-0.21808884753169328",b"-0.2223245183509539",b"-0.07413486190970431",b"0.024864138902692342",b"-0.1153337267046991",b"-0.15066485518534198",b"-0.12589160638463648",b"0.4785381165990663",b"0.16586503172356573",b"0.12635887682921348",b"0.03293334219814023",b"-0.6193091730909752",b"-0.3327439708604792",b"0.2021743080545968",b"3.4467547391071336",b"-0.2206538500767684",b"-1.4095762385707902",b"-1.2967981100964043",b"-1.1953290954734435",b"1.4682100225933146",b"-1.4391390870217098",b"1.2777102461409098",b"0.3040419276915216",b"-0.13487031443290853",b"-0.70033847675002",b"-1.2866327978166887",b"0.14632739230640945",b"0.1260479477422124",b"-2.6474305458894998",b"0.0",b"-3.747177226739183",b"-0.29359227738985216",b"1.045652399857895",b"0.36868256176532427",b"-0.0083179686181305",b"-1.6786042787698925",b"-0.19794838179360041",b"-1.5589668775257528",b"-0.7611826106152297",b"-0.3475233495138399",b"1.9737961741801677",b"0.5050938861917019",b"-0.6846848540981794",b"0.211900469474414",b"0.0",b"0.0",b"4.285687384786814",b"-1.034169458732864",b"-1.4596886923288612",b"1.0690403750262611",b"1.054260920028031",b"0.7320993168054125",b"-1.0345040150214038",b"-0.5089958863240283",b"-0.3021917050519328",b"-1.4885234855524025",b"1.238754769658765",b"-0.3022745564555315",b"0.7106750666012065",b"0.0",b"0.0",b"0.0",b"-3.4737496814970767",b"2.2902969604043877",b"-0.7970718761754261",b"-0.9970148919737308",b"-0.5202292664362369",b"1.7327072332969833",b"-0.740858718265333",b"0.10660044387438647",b"0.3951930817740925",b"1.7874975557737154",b"0.9985220786217512",b"1.3698745750005776",b"0.0",b"0.0",b"0.0",b"0.0",b"4.628810693646948",b"1.3315396280405247",b"0.20665919254975873",b"-0.15561787777235292",b"0.7959588607721608",b"-1.3935773418564572",b"-0.41378010774445073",b"1.7265974123321242",b"-1.427379772440808",b"-0.22030556371757004",b"-0.5472191615706578",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"-4.111001520252805",b"0.3293237319610791",b"0.2661713614171426",b"0.08447955366994686",b"0.31933202318051224",b"1.1808440914874758",b"2.0236626990568576",b"0.051579266491622366",b"0.10425592619017335",b"-0.6007760480963393",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"-2.297828555968957",b"1.3852651310448962",b"-0.11750055065490606",b"-2.110530821094497",b"-0.03556131263602863",b"-0.014894156242636458",b"0.6544070761615823",b"-0.8945635073155728",b"-0.3116111465969693",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"2.9147223944029608",b"0.42948543553520413",b"0.7087784476594604",b"-0.6127711278833896",b"0.1455345738468593",b"0.7124063017725195",b"1.629250866987188",b"-0.8951088028613263",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"-1.6861734870611997",b"0.4521001438015455",b"-0.016393598744860016",b"0.263918317247812",b"2.024551298736872",b"0.2860694250005872",b"0.382573725589046",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"-2.396690528638734",b"-0.9432900966080768",b"-0.443695092687483",b"-0.6667213860326702",b"-0.4831894365965896",b"-1.5781893001407772",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"1.7518324292199199",b"-1.2377920576953572",b"0.5142285228959983",b"-2.0049805501442655",b"1.1757934672374688",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"-1.352479200736254",b"0.7473640462196147",b"-0.13998006558158663",b"-0.8227559870767829",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"-1.9136944621512264",b"-0.9780957431383559",b"-0.40897027092863086",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"-0.41375538977819687",b"0.09154047209222393",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"0.0",b"1.4069008958603817"]
for i in b:
    io.sendline(i)
io.interactive()
    