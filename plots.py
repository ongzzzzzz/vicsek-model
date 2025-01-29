import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

noise_values = [0, 0.1, 0.2, 0.30000000000000004, 0.4, 0.5, 0.6, 0.7, 0.7999999999999999, 0.8999999999999999, 0.9999999999999999, 1.0999999999999999, 1.2, 1.3, 1.4000000000000001, 1.5000000000000002, 1.6000000000000003, 1.7000000000000004, 1.8000000000000005, 1.9000000000000006, 2.0000000000000004, 2.1000000000000005, 2.2000000000000006, 2.3000000000000007, 2.400000000000001, 2.500000000000001, 2.600000000000001, 2.700000000000001, 2.800000000000001, 2.9000000000000012, 3.0000000000000013, 3.1000000000000014, 3.2000000000000015, 3.3000000000000016, 3.4000000000000017, 3.5000000000000018, 3.600000000000002, 3.700000000000002, 3.800000000000002, 3.900000000000002, 4.000000000000002, 4.100000000000001, 4.200000000000001, 4.300000000000001, 4.4, 4.5, 4.6, 4.699999999999999, 4.799999999999999, 4.899999999999999, 4.999999999999998, 5.099999999999998, 5.1999999999999975, 5.299999999999997, 5.399999999999997, 5.4999999999999964, 5.599999999999996, 5.699999999999996, 5.799999999999995, 5.899999999999995, 5.999999999999995, 6.099999999999994, 6.199999999999994]

# r = 20
r20_v_avg_values_1 = [0.913709792359895, 0.9576314537581485, 0.9415654313309832, 0.9206742795893567, 0.8526133881352261, 0.7759175701224154, 0.64748191096391, 0.5153357094309335, 0.30541711088223333, 0.3474569810453634, 0.3927233268973251, 0.36608119422034635, 0.1814121797575872, 0.20640611238158668, 0.20377565250175908, 0.13913870298244677, 0.09808749635122067, 0.16511687331091032, 0.06536138474055861, 0.1381204175150045, 0.10552104857252997, 0.02012502302310179, 0.022081698181121334, 0.08289953776587036, 0.057305834420194164, 0.10788422114555021, 0.04952260718021856, 0.10151565312203581, 0.02856396974870745, 0.06503948955315232, 0.014466142554820543, 0.05750018840524677, 0.058029190907910144, 0.03750993010028759, 0.061839990267221416, 0.09443706409295875, 0.04805475645052001, 0.07898373028381499, 0.12564090110063258, 0.01898530289479465, 0.05344158935551765, 0.04112407940755126, 0.05444506030015175, 0.040349526682126775, 0.04840023730781745, 0.04652539973328436, 0.07721108870531393, 0.05688716479320596, 0.07317280749258108, 0.041786202731888815, 0.046597438340692514, 0.026133072558996745, 0.006722037119179106, 0.07624973332105704, 0.015267398873683294, 0.033463952992831954, 0.06385306731472394, 0.042344495012738174, 0.05533235862142478, 0.026759198938698252, 0.008277310559676534, 0.06907334451806853, 0.019442120259164388]
r20_v_avg_values_2 = [0.9810302964709489, 0.9694137050208834, 0.9240414050648862, 0.8991284964604753, 0.8211358986123724, 0.7180824335855459, 0.6486377773288342, 0.4762666178988724, 0.4500111743663298, 0.3370607616020085, 0.24461790131977657, 0.24446544906523932, 0.3597384042933758, 0.09000073777515111, 0.09590831979288438, 0.1155729748026875, 0.00588084676818679, 0.06750198019623857, 0.11844913040361683, 0.05990617165794043, 0.09737149964777359, 0.044615496238584566, 0.1133639161688727, 0.02688455884863681, 0.029261638665032418, 0.04196489933988794, 0.060673665502795786, 0.05047656801168704, 0.07684115476053502, 0.10686138241825134, 0.015048903163287948, 0.031516016483851585, 0.09130367531195639, 0.04097819858503294, 0.04645702894577443, 0.029992803534502437, 0.06837069260118372, 0.024732505517443423, 0.017946556605760316, 0.018060765925412853, 0.037051294103150605, 0.043765772840148265, 0.019714045295339214, 0.029112927127428696, 0.07615886098430663, 0.012588223781300478, 0.0707177363574769, 0.01994492796597729, 0.03984344683201367, 0.019845965394885392, 0.038339579304883166, 0.02995491847858474, 0.014467435778892408, 0.03619456414331071, 0.020904701389882166, 0.09365262571990512, 0.01549746455069697, 0.036821956527155114, 0.0641780343838384, 0.03499355304007229, 0.02364203872350716, 0.03598112094951287, 0.04960828467448851]
r20_v_avg_values_3 = [0.9906879659988216, 0.9725217659668078, 0.9449730006189021, 0.9359787491822246, 0.891119135764575, 0.6718681381342229, 0.6837291685668581, 0.536262380234166, 0.5680707010459134, 0.5862216148329552, 0.23027037195483976, 0.35426990777044753, 0.3115582338665371, 0.310574795429488, 0.17321361856740555, 0.11355611620704675, 0.08161676332318833, 0.17328809453398966, 0.044494579954621125, 0.05986647214601834, 0.0872870987273178, 0.030823640818067866, 0.05212871323427065, 0.09181542551480787, 0.039131516387838926, 0.00876985369442375, 0.0877082721777662, 0.05635599312831978, 0.03531072005133781, 0.10631028869470807, 0.04539481851438037, 0.0231592235189003, 0.07411090767868278, 0.018526767582809377, 0.0786721990822935, 0.050493960502295106, 0.05086836404301543, 0.05209771925283654, 0.039009276946829305, 0.037803006837260095, 0.04758608796853545, 0.038746523724407095, 0.02823138331453165, 0.05583512982471011, 0.022450641284819557, 0.0780381244616287, 0.030703511960759728, 0.07218287116911869, 0.07004952160295423, 0.06899406385528588, 0.011512013954503048, 0.04070159088239793, 0.06492605141166549, 0.07465253907213923, 0.02118395531995896, 0.03692542112746663, 0.026938805438709783, 0.05756694374823374, 0.03888460395290708, 0.021738093758114065, 0.0666551422978894, 0.016215717532691257, 0.030802488686044537]
r20_v_avg_values = [(r20_v_avg_values_1[i] + r20_v_avg_values_2[i] + r20_v_avg_values_3[i]) / 3 for i in range(len(r20_v_avg_values_1))]

# r = 40
r40_v_avg_values_1 = [0.9960097861626748, 0.99632915667359, 0.9657924423457291, 0.9450265798485887, 0.928091655500178, 0.9372303680069538, 0.7857085982490368, 0.8352746579665882, 0.8996091492210038, 0.764552824281597, 0.7158003681090119, 0.4363921772386392, 0.6143869695006063, 0.0763349433613807, 0.450958118483301, 0.4236313361494995, 0.6648862488939636, 0.1815769145966691, 0.22759009500909508, 0.4649530823575906, 0.26668813839937244, 0.26341172023680953, 0.1671165647232752, 0.182359604400444, 0.1475115712215026, 0.16369168915212495, 0.27398861573546157, 0.0501433320892477, 0.1251988146007731, 0.08025569800141855, 0.07825741976688691, 0.1322954855708732, 0.1534829566507176, 0.1876864962410779, 0.09028932862786883, 0.08775478224079518, 0.036987221532882475, 0.012405550897841002, 0.06841131221440525, 0.046197913764091186, 0.03165669835985186, 0.059236886895398966, 0.013702902711865675, 0.026919061697316945, 0.05389091188244519, 0.06877957300890739, 0.03154371041821749, 0.04513311453963964, 0.025923083508033233, 0.0923472676430297, 0.002484925040922896, 0.046883402676491805, 0.028869958013598585, 0.058122297723040284, 0.026386372493145113, 0.04353259312847054, 0.040860814313082215, 0.07557940513523789, 0.018055482289504744, 0.021075770313748177, 0.056584793161385316, 0.0058020726322572415, 0.06607945886370341]
r40_v_avg_values_2 = [0.8133484869150146, 0.9960932761482428, 0.9964576530019349, 0.9860135050934529, 0.9439581566236209, 0.7688065620043054, 0.7221516135031916, 0.8969855199401943, 0.9047266180577451, 0.7881461908916796, 0.8182256774576143, 0.5337431685494043, 0.3882942437014986, 0.3358774704935859, 0.5609015198344585, 0.6186781080909138, 0.3520677715975716, 0.397509697374197, 0.34094726089767696, 0.16227746479073288, 0.43875303489680434, 0.3952042452089541, 0.37926087868425473, 0.013253130432606314, 0.16570941779446144, 0.16291621375407095, 0.06429500212871916, 0.056267376472211236, 0.08842263890153329, 0.07757719837074935, 0.1937300841083146, 0.02798573308268143, 0.018708583246502267, 0.08877727477326389, 0.16890472959567293, 0.10690631236016439, 0.05481682079194574, 0.05298807806511987, 0.059407798527077886, 0.050353132446911746, 0.05744669804363383, 0.028388556147909815, 0.010700316935910012, 0.03951132002388843, 0.05802737972797536, 0.05433440166612572, 0.009481610962064941, 0.0653352553529228, 0.06316649102904096, 0.0491035831954574, 0.09530914741150695, 0.03201396062671597, 0.03980250162816949, 0.05221382445634426, 0.042479674466730594, 0.03223521275705378, 0.014787503542540732, 0.03698997181214408, 0.004636086275379939, 0.04285225628129733, 0.04820373362888035, 0.07477769021916109, 0.05901563285822032]
r40_v_avg_values_3 = [0.8235212355691996, 0.9985561681884899, 0.9750153049042224, 0.991345326485538, 0.984218861232616, 0.9718127587920922, 0.8174857998657132, 0.7796128998238355, 0.885907081519277, 0.651244850753797, 0.7399126477027584, 0.7044234554681468, 0.5554705011472448, 0.5722596914089291, 0.6003637679677473, 0.46112781645931566, 0.5600225274319001, 0.1968193516595786, 0.2313424990253431, 0.17884957146248834, 0.26330672634717384, 0.11048138782435933, 0.12475430252246211, 0.19193795106375755, 0.02920920593475121, 0.19883621334567356, 0.148804635013203, 0.059747874958515, 0.1059747481059387, 0.04556570827653337, 0.041622213383460976, 0.1271122359988578, 0.14799841615419945, 0.05386851919013639, 0.12147358509963235, 0.039601029290355624, 0.022799127741831623, 0.11613460737455157, 0.13349042138188866, 0.04161783322605227, 0.02902245825616849, 0.0560205720711552, 0.05496165034425202, 0.01294309873813548, 0.026444235403358655, 0.0914514426373655, 0.126310519821602, 0.030644328226495966, 0.04396130769886342, 0.07408775981523583, 0.01325871046572275, 0.06278315347916796, 0.06853779790688652, 0.03169417393797525, 0.06697058308977118, 0.03978941807670632, 0.002306814186494263, 0.01331520231304206, 0.0755257357463152, 0.0264661576101094, 0.02348180159959945, 0.033359209322340204, 0.015828733983071164]
r40_v_avg_values = [(r40_v_avg_values_1[i] + r40_v_avg_values_2[i] + r40_v_avg_values_3[i]) / 3 for i in range(len(r40_v_avg_values_1))]

# r = 60
r60_v_avg_values_1 = [0.999972849714014, 0.9964560446008984, 0.9937054673200164, 0.9838105133357536, 0.9655153153885644, 0.9691267170806512, 0.9753562933338502, 0.9283031371496202, 0.7749970269138797, 0.8079400590818955, 0.8255060010823682, 0.8386760146472481, 0.7567065133119357, 0.6223640347676199, 0.5883755580745221, 0.7108769615889129, 0.6222133966003001, 0.6651446772231058, 0.6294203194156063, 0.6391222041037037, 0.6393649869509337, 0.4772627352078601, 0.450079670353059, 0.3227010759046811, 0.2908506574591454, 0.510507030837804, 0.4966798335958892, 0.32810441380729705, 0.38465917386592696, 0.40738755278420163, 0.18929686229272283, 0.18359138032967334, 0.21237243527955207, 0.26275880150151026, 0.32548112329369155, 0.022093734685624027, 0.18456029356462159, 0.18658836693747807, 0.029049286520929862, 0.08055204071191525, 0.10435974611339036, 0.12058468513881775, 0.05104319340116617, 0.06284642219448856, 0.17030999656860635, 0.1100102542880391, 0.13303551933519112, 0.09512976125392929, 0.07241664324136853, 0.06279803074914743, 0.059664996715421525, 0.035383534041635654, 0.01828214767531987, 0.055580175524852754, 0.018861453113001442, 0.060455060105689275, 0.07817652407177132, 0.055662399957373446, 0.02684965126180249, 0.046750445628835714, 0.0601492839534, 0.0970317787654454, 0.029255556567410565]
r60_v_avg_values_2 = [0.5665842238915073, 0.6561305167373078, 0.9656479238376666, 0.9892443576437626, 0.9392001894621583, 0.9564766227010685, 0.8733479734597451, 0.8903841269120837, 0.8630123428643043, 0.9332545779115459, 0.8193876143004757, 0.6845536475235012, 0.7298345060853185, 0.8116481147771706, 0.8203814319222242, 0.7417525284170924, 0.7220361373129156, 0.6471170856764886, 0.7067139667263845, 0.3407989226614574, 0.5657693034896355, 0.42185381969824765, 0.4732113395350583, 0.16572208645640651, 0.3295436531822005, 0.4293602963646617, 0.30658072716058576, 0.3131690823954643, 0.12813401069174854, 0.21096117885705284, 0.19803781152024938, 0.312427579704207, 0.2181566868833782, 0.18917324446191633, 0.1505785112386162, 0.139147616980834, 0.19194987259096538, 0.10988929413091234, 0.18626072741605185, 0.14213203571570204, 0.06603431869499432, 0.213080186966366, 0.10805416984116321, 0.16266933272794873, 0.09789160408959846, 0.02814505748238992, 0.025723286604621264, 0.10981249572355027, 0.03840704723901228, 0.05919310397598324, 0.03870089087964205, 0.059688197456920424, 0.05054730969494301, 0.0955305655084262, 0.055162789151050134, 0.06911854304173218, 0.054663875741863016, 0.030225958390355828, 0.013253038757684648, 0.03418927072643108, 0.024135320653644012, 0.019194350701581327, 0.05900534338061168]
r60_v_avg_values_3 = [0.9999998670375967, 0.999528586723748, 0.997382840769612, 0.9910260936939919, 0.9810376578177935, 0.9615336618626179, 0.8947422170480921, 0.9549979880300887, 0.9057993057379664, 0.8661038733926495, 0.8848197317875028, 0.5420461545164678, 0.7677169339594788, 0.7112872209879685, 0.5645535810715056, 0.706548497256122, 0.7096199499550249, 0.6425727883466935, 0.5428228464599693, 0.5682518577318638, 0.4445849085383419, 0.616607423048931, 0.4267204268888461, 0.2864739932939406, 0.4769999038451064, 0.1325121869852548, 0.2893269357628354, 0.20487613512135863, 0.27437470829792954, 0.26931238732375906, 0.2337208916686898, 0.2978376613956839, 0.30149096448015, 0.18513719660287867, 0.22052461680736477, 0.0743666318508546, 0.22029259179502628, 0.12735927887519896, 0.14197700089681387, 0.16091040013099508, 0.08920550206502895, 0.18010944802566334, 0.12946897215603484, 0.17842615266642448, 0.1435224654090109, 0.08900554449065742, 0.09917630566273943, 0.09583300338897745, 0.1141235064953749, 0.04502791256944576, 0.04001199748287242, 0.03526087054062655, 0.01608930378769885, 0.013222578872854558, 0.0692353592816537, 0.042424485736709455, 0.0524022942665369, 0.024884402405997173, 0.013771809699772486, 0.06382580099514061, 0.0659737148886341, 0.07504923093513745, 0.02057263039364787]
r60_v_avg_values = [(r60_v_avg_values_1[i] + r60_v_avg_values_2[i] + r60_v_avg_values_3[i]) / 3 for i in range(len(r60_v_avg_values_1))]

# r = 80
r80_v_avg_values_1 = [0.9999999996831072, 0.9990638234457976, 0.9976903408497434, 0.9902783750177381, 0.9868334719986236, 0.93981255621032, 0.9738270981834688, 0.9656392840065191, 0.966146423165688, 0.8922003568048708, 0.9206416526298992, 0.9097761743165789, 0.8226756184719414, 0.8762038214684924, 0.811541702844637, 0.8648610699140011, 0.49407693659795293, 0.6474045869885442, 0.7212644373444628, 0.7589610398416333, 0.7285758239943654, 0.6457036982322215, 0.6394062857858067, 0.5419732921240249, 0.693887980319871, 0.528246676591706, 0.37465463295027696, 0.4998389503324852, 0.3922143055027048, 0.12877135650831087, 0.3662333593715356, 0.5112377648351284, 0.4655377210258194, 0.3883697481224483, 0.15782219621846214, 0.45801454522003976, 0.2671865701738185, 0.22132774560055826, 0.26001688888494123, 0.2571320858246092, 0.22818311771435473, 0.2288924256472934, 0.19134734794362604, 0.18306579721233182, 0.08789238257903965, 0.15857515496848532, 0.18271901945289604, 0.2127562916662342, 0.10149529269658122, 0.03620405275489546, 0.13063498300924117, 0.10311433298754609, 0.05649410828337826, 0.03227143530109898, 0.07444472865654644, 0.06801538596977896, 0.05777352907967111, 0.043664411107132345, 0.07639427654703769, 0.03931344184284137, 0.02506837966587996, 0.033786570437017875, 0.05891142222616286]
r80_v_avg_values_2 = [0.997118278752943, 0.9990510782326328, 0.9947467012392196, 0.9891103799715262, 0.9888794592130413, 0.9099884162054696, 0.9590095386581788, 0.9494739314420231, 0.8653988141024541, 0.9476893768411853, 0.904057681235409, 0.8827723174657482, 0.877293050918487, 0.8611633516045164, 0.8043636795440912, 0.8301939428426229, 0.7643719608989271, 0.498759677713956, 0.8072723062774818, 0.568563808310118, 0.7558060114113023, 0.625268959031391, 0.6410706640622338, 0.6245935338973313, 0.6234308446865374, 0.6141917026025601, 0.4724422157566068, 0.41180359381389475, 0.56896196503628, 0.41084960273229204, 0.41381699658336096, 0.19348472334271616, 0.3685118687761604, 0.2759422094749583, 0.32659143369984117, 0.24396202190697347, 0.3740728121948388, 0.2796566375534119, 0.23579530490849795, 0.28408736392519374, 0.3172397901831462, 0.22316341479327964, 0.11477815718532818, 0.04523647992677002, 0.1312268552264677, 0.1641045367355384, 0.13240252254630874, 0.13007665420843997, 0.0573556516804008, 0.11685709939512126, 0.07425086339554458, 0.02588856658535924, 0.11994567658096258, 0.040539244892008885, 0.029936723455686164, 0.016269595966807767, 0.053458873957532196, 0.04430119815420295, 0.012370820600062135, 0.07063880797793802, 0.03572779296661281, 0.09206672571435066, 0.034160066562748885]
r80_v_avg_values_3 = [0.9999999816527501, 0.9988747050437011, 0.9962632790536864, 0.9915908534664041, 0.9795751210056478, 0.9832080359920675, 0.9691354724870563, 0.9466090328458359, 0.9309216130255276, 0.9281985347916352, 0.9194384650194438, 0.8881840108570608, 0.8609107219328808, 0.8145222431780297, 0.8251778532541466, 0.6359798684641481, 0.8300245933806971, 0.8375119068005922, 0.8457080334212361, 0.7835440239547863, 0.7189578766772944, 0.7016467462122722, 0.43618576833978695, 0.3464723128682405, 0.5752756445381351, 0.20716988512409823, 0.25161303197162666, 0.4701126677843318, 0.46213805927125473, 0.486997149577675, 0.5048690165225225, 0.4352268574804646, 0.32059416204618885, 0.255795307546508, 0.36170961239850663, 0.273380297564099, 0.3541804672374159, 0.23376103758617242, 0.19810731626100178, 0.2822331178636386, 0.19333567252951245, 0.11740922052417035, 0.14668391228409833, 0.18346849322042658, 0.22491251418274552, 0.13277943471249776, 0.08981493012797201, 0.07678483122373014, 0.13981146376626397, 0.010966930696553676, 0.1540004259683888, 0.08673648994720422, 0.05098387812514463, 0.02741048649905945, 0.00586164446817588, 0.03934441922415257, 0.07144528278768875, 0.023576413066368616, 0.06804906358919771, 0.025703201321683196, 0.05238422038784577, 0.07133206926483157, 0.02891080725086567]
r80_v_avg_values = [(r80_v_avg_values_1[i] + r80_v_avg_values_2[i] + r80_v_avg_values_3[i]) / 3 for i in range(len(r80_v_avg_values_1))]


r20_v_avg_values = gaussian_filter1d(r20_v_avg_values, sigma=2)
r40_v_avg_values = gaussian_filter1d(r40_v_avg_values, sigma=2)
r60_v_avg_values = gaussian_filter1d(r60_v_avg_values, sigma=2)
r80_v_avg_values = gaussian_filter1d(r80_v_avg_values, sigma=2)
plt.plot(noise_values, r20_v_avg_values, label='r=20')
plt.plot(noise_values, r40_v_avg_values, label='r=40')
plt.plot(noise_values, r60_v_avg_values, label='r=60')
plt.plot(noise_values, r80_v_avg_values, label='r=80')


plt.xlabel('Noise')
plt.ylabel('Average Velocity')
plt.title('Average Velocity vs Noise')
plt.grid(True)
plt.legend()
plt.show()





r_values = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

# n = 0.1 pi
n10_v_avg_values_1 = [0.634369047094349, 0.38116925528954343, 0.555151488273928, 0.6128493840020943, 0.6292098834653886, 0.6808075979877009, 0.7252994649800996, 0.658295102052384, 0.7208469462538069, 0.8561389715600037, 0.951893970778435, 0.961927398433228, 0.9649362654586434, 0.938634396326008, 0.9745280396959489, 0.9639202362989187, 0.9840938339662681, 0.9642561017438416, 0.9809984194899029, 0.9768038811616614, 0.9713603031762403, 0.9925011337768297, 0.9886895089455688, 0.9798440914722605, 0.993463644334498, 0.990045991802184, 0.9946589370450617, 0.9934420757161768, 0.993732317898248, 0.994184066309727, 0.9944122031956288, 0.994354279328169, 0.9942046884151701, 0.9933596920279645, 0.9859928306013632, 0.9936547332162615, 0.9918343324874028, 0.957866700084296, 0.9947841785823619, 0.995100656958825, 0.9954845887126547, 0.9701483132036198, 0.9901563770561108, 0.981336454629227, 0.9887410032487342, 0.9801033798840828, 0.9938808056849093, 0.9911580626566485, 0.9874627262289702, 0.9894544019867092, 0.9866872739245799]
n10_v_avg_values_2 = [0.9311335840579419, 0.37680365495839335, 0.6005886444396783, 0.6915800187819108, 0.7301046330602909, 0.7174904890813559, 0.7988224635963328, 0.7159898820163477, 0.8378192380250875, 0.8432787545262822, 0.8515860219908659, 0.9064776076320289, 0.9037461647089472, 0.9061883255479695, 0.952408129742209, 0.9417168880523769, 0.9649171119879099, 0.8768554906158745, 0.9388807938001635, 0.6772930447946129, 0.9264835472192609, 0.984453644404051, 0.978755540520072, 0.9811239366515888, 0.9852369040773877, 0.9708914546832931, 0.9771767165140668, 0.9577934483010259, 0.9826284450134901, 0.9925374399411118, 0.9183956051140294, 0.9937726269592813, 0.9829208181749027, 0.9843509730104407, 0.9593319623957386, 0.943294735268142, 0.9810787070939356, 0.976049062199526, 0.9868116412303544, 0.9899267778151909, 0.9896538965379218, 0.9683392324561715, 0.9948856821388725, 0.9602141289333128, 0.9729522605853603, 0.9575719427294755, 0.9848331861439612, 0.9915231193175913, 0.9944792897874606, 0.9931853769026501, 0.9894485966373466]
n10_v_avg_values_3 = [0.9208460336419618, 0.41523722004491576, 0.5569451976709434, 0.6425612658589507, 0.6531277777792585, 0.7846822396108712, 0.7640771793723586, 0.7881212639856009, 0.7427433730029457, 0.8730881345153366, 0.8457197518132091, 0.8499538472533651, 0.8585010420453792, 0.7880695362897436, 0.9604761387958921, 0.9799438125769048, 0.9399293623247218, 0.7608930313846551, 0.9391403772687675, 0.9776650204676351, 0.976189971322536, 0.9817920095129022, 0.9879628670378151, 0.9465007078879788, 0.9821980254299171, 0.9576079614962458, 0.991096572853419, 0.9755821289347532, 0.988571560406694, 0.9906973639498848, 0.9895280838664788, 0.9840027373764926, 0.994599458212565, 0.939806201435399, 0.9863010426045377, 0.9914143528437102, 0.9863483539830309, 0.994633705437403, 0.9872330999453127, 0.9811617053570079, 0.9793529045616901, 0.9932405571424039, 0.9916112227349906, 0.9944307695648196, 0.9940918924524375, 0.9915216300215708, 0.987484782456539, 0.9921207637294722, 0.9926411681606975, 0.9797435797928251, 0.9917406738115612]
n10_v_avg_values = [(n10_v_avg_values_1[i] + n10_v_avg_values_2[i] + n10_v_avg_values_3[i]) / 3 for i in range(len(n10_v_avg_values_1))]

# n = 0.2 pi
n20_v_avg_values_1 = [0.5853137152211646, 0.022018083603678126, 0.1620984778858359, 0.16618844673016928, 0.2660699357574603, 0.420589866547444, 0.25188385236857386, 0.3934423492746249, 0.6156841652752504, 0.708329477723903, 0.6172243877798375, 0.7544559504041756, 0.7325487998598804, 0.8038327419092411, 0.7981966884502358, 0.8503644485949691, 0.7645863834796764, 0.8663019776866504, 0.8134702245209049, 0.7960561296399129, 0.896554926651883, 0.7414624354853295, 0.8212070968954296, 0.9333618950793355, 0.9026567764260247, 0.909412258827545, 0.9208904339419586, 0.9559103048736699, 0.8699586030403621, 0.9094990175643358, 0.9205259045622133, 0.933982815843259, 0.949657416691783, 0.9107608487419145, 0.945514602437799, 0.9690019299973504, 0.9652869353589151, 0.9728523078949456, 0.9763130273783664, 0.9437334342084075, 0.9664856587363403, 0.9597651740140793, 0.8909152397167369, 0.9571680563830884, 0.9758159300088314, 0.9686256440079419, 0.9554308406704116, 0.9574520464492519, 0.9752436074956555, 0.9755148612200616, 0.9583308719341659]
n20_v_avg_values_2 = [0.7234884013411038, 0.0789804815152751, 0.13764784868391122, 0.22921477726412542, 0.2557052188033223, 0.4167395335325525, 0.35416969472174864, 0.4588626156276672, 0.5450088211189361, 0.40744739520578643, 0.5690277139195599, 0.5939689438562498, 0.7962142660601864, 0.5934011337313156, 0.8589301080245394, 0.8613314912824961, 0.8417659969868843, 0.9195891406498907, 0.8237069222118516, 0.9020623826364744, 0.9324929691614859, 0.9048633835521125, 0.8758202044654567, 0.42402582453289095, 0.5687480490915152, 0.8324886608746339, 0.8283783802725143, 0.9446515979479194, 0.9594392983514857, 0.9620706028085029, 0.9461755732047848, 0.9519707696222421, 0.9164767289806753, 0.9673573752908654, 0.9592685012657659, 0.940422974431828, 0.941312507486124, 0.9113642393917415, 0.9436303770037662, 0.9241858621125283, 0.9414342176804859, 0.9681708075641098, 0.9711550210117877, 0.9705281571072383, 0.9558027798354225, 0.9644643766728359, 0.9618561929790587, 0.9748626855232732, 0.9781983947773313, 0.9747376867952692, 0.9781916750781855]
n20_v_avg_values_3 = [0.6476403439253702, 0.020311279843952663, 0.12061654625396892, 0.21664669063771835, 0.2927056587666765, 0.39526065334213584, 0.30961808558198944, 0.5553800727022092, 0.6889255786583874, 0.6775342201662063, 0.639515760478018, 0.5676857937514613, 0.696839708789225, 0.7260517976115668, 0.6325194135556607, 0.617518898894382, 0.8321876694359522, 0.7667362812487228, 0.7790300732661906, 0.7671838601457216, 0.9279107842468864, 0.8107719439244053, 0.8806971871645777, 0.9546207844045225, 0.9334079596718305, 0.857719453358581, 0.9389903978059072, 0.9480075045211129, 0.9355549872215675, 0.9244308824076658, 0.9463800526098439, 0.9658924693117078, 0.920111424788782, 0.9680106372904936, 0.8594513853604335, 0.9686105977699311, 0.9568505620415878, 0.970547480282025, 0.9632829802755579, 0.9632450379423038, 0.971783993340857, 0.972487775557937, 0.975316766200383, 0.9595131838787061, 0.9402528452995739, 0.970043223908346, 0.9755424718341791, 0.9789123688638713, 0.9778409938792876, 0.9141154300323381, 0.9753831168480277]
n20_v_avg_values = [(n20_v_avg_values_1[i] + n20_v_avg_values_2[i] + n20_v_avg_values_3[i]) / 3 for i in range(len(n20_v_avg_values_1))]

# n = 0.3 pi
n30_v_avg_values_1 = [0.3318774530844532, 0.03261487616957679, 0.05800043517722545, 0.035442130495713535, 0.09452089963793878, 0.20274590349399965, 0.06558369375465338, 0.2928394575438918, 0.3098583703793799, 0.4311927646916515, 0.3231795727948879, 0.5695392840453782, 0.4508173281683907, 0.6849263454405465, 0.5477364293699077, 0.585444854195033, 0.733806484739287, 0.7190618423688695, 0.6972096774523178, 0.6276507222942911, 0.8061758398840999, 0.6402007123544252, 0.6299681027139687, 0.7726913761554424, 0.837985899377622, 0.7929924706238467, 0.739565637381664, 0.5415092971167063, 0.9287421634194609, 0.9020609451233816, 0.91438854812742, 0.8508695425790177, 0.9049297235724068, 0.9006763612960894, 0.8120470909789249, 0.8055182094001359, 0.9164600622281185, 0.8980285018702199, 0.9413039237996805, 0.8293687887252907, 0.9234997823630932, 0.908065559308612, 0.9174558010812147, 0.9434215681939625, 0.9307736349176904, 0.948382713395312, 0.9506014257338805, 0.9419830268648861, 0.937521111746754, 0.8577690010581039, 0.9151477893684781]
n30_v_avg_values_2 = [0.41169835654327086, 0.02955906880889374, 0.046595985502822616, 0.06089205667912317, 0.13927558733030773, 0.1367390419221415, 0.16021505790687146, 0.2772539072965066, 0.19024563737444075, 0.4991422601053536, 0.4798049159533487, 0.30719862144354376, 0.516038844241207, 0.5288025772202555, 0.6295202154911805, 0.6425217431226747, 0.7007566624270042, 0.607665056345452, 0.7344396924346367, 0.7334293943861477, 0.6489033974275583, 0.649938406232913, 0.8077406902378756, 0.7553115124677752, 0.8402169736332635, 0.8255184020269787, 0.7078279480472301, 0.7800520838136117, 0.8755800972935085, 0.9148074287545548, 0.9275325275688927, 0.803269970415025, 0.826796737462503, 0.8729600205439337, 0.917673310205806, 0.8866642263752699, 0.9229927000580955, 0.946446482467059, 0.8959651573021432, 0.8479648246737648, 0.8618279159107469, 0.8948534254525409, 0.9045980782909131, 0.9237418956629779, 0.8796379821461917, 0.8498665319061705, 0.8841874331413412, 0.9391307779198897, 0.9272570771485006, 0.900407095840676, 0.943640767198141]
n30_v_avg_values_3 = [0.36269571889590707, 0.04642996285227294, 0.08368260767638007, 0.06349593165556382, 0.14386162159168983, 0.07027178142071121, 0.07732124532515906, 0.3119074805802873, 0.32940675872481734, 0.5243510136928468, 0.31459939398570147, 0.558047093906804, 0.5481674189066199, 0.5824327441555983, 0.6783745198539627, 0.4361068444976783, 0.6053939664431184, 0.7356572950931656, 0.7009509448385094, 0.8699228048821033, 0.4993301444458867, 0.6079087257501977, 0.8419148957650939, 0.8974098287970952, 0.8797713180444677, 0.811450686008893, 0.6715439294997932, 0.7163120271150545, 0.7882221111600485, 0.839965230414321, 0.8607852489451571, 0.8817201638777559, 0.9094034059574961, 0.8378606124294632, 0.8587171787573199, 0.8893126709477249, 0.8832757486483119, 0.8906708885331613, 0.9261149558101126, 0.9315442616072432, 0.9311837055016265, 0.9122715963237819, 0.9392009327714739, 0.8929639357693175, 0.9583094845391067, 0.9512562714230979, 0.9538065230892147, 0.9490123990149215, 0.9420843294215644, 0.9225674234825657, 0.9338113583242057]
n30_v_avg_values = [(n30_v_avg_values_1[i] + n30_v_avg_values_2[i] + n30_v_avg_values_3[i]) / 3 for i in range(len(n30_v_avg_values_1))]

# n = 0.4 pi
n40_v_avg_values_1 = [0.30677137364884094, 0.044841320937431324, 0.07827971667718532, 0.0618893948278361, 0.09025841734707488, 0.12002482178011792, 0.07897464621440378, 0.14790471132376698, 0.061749578659416576, 0.01033258619504629, 0.02731863731404811, 0.3932064587768431, 0.36973826500973445, 0.4906748247752768, 0.46035558550343025, 0.26712691294482077, 0.4850429411692051, 0.45215104375584914, 0.28699423728133183, 0.45721643732120115, 0.5569866739577137, 0.7400504531658738, 0.42319874164714855, 0.5551323215319794, 0.7517572869433824, 0.7662864289842758, 0.7743405189048718, 0.794565237627443, 0.7824133456980938, 0.7057366344840855, 0.7098561574762261, 0.8415766534691848, 0.7580016106100408, 0.8365469000369079, 0.8896577903990586, 0.7728859005907789, 0.795687606696978, 0.78651715065436, 0.8894245247807939, 0.8534073819855102, 0.8878096585145393, 0.8874554494983237, 0.8608489339744175, 0.8581748809495431, 0.8634169059307155, 0.8502456940657384, 0.8804601635338616, 0.9029863549765075, 0.8625398098642753, 0.866908585593614, 0.8734920231252467]
n40_v_avg_values_2 = [0.23577002818980994, 0.0706907782392978, 0.043181345303960096, 0.037468652756069594, 0.10953135221072588, 0.11683652900019435, 0.09188084612222211, 0.11603468105290633, 0.13217560879778192, 0.10951851899377706, 0.13993701616012744, 0.2777687464610606, 0.3772489387465224, 0.1730809016455787, 0.15253634194526677, 0.3474350610397753, 0.531921127214727, 0.30024092378424183, 0.4857782285486269, 0.6246013532533787, 0.5926260655436276, 0.6670468606492456, 0.5361452778178774, 0.7477201846411589, 0.6007187529495761, 0.7705217840424158, 0.7829928414158829, 0.677570462276029, 0.7377904594658733, 0.7356670949232095, 0.7897578058923601, 0.7145576625254492, 0.7158894157410497, 0.8226012538156134, 0.8177644152732443, 0.8764376396827991, 0.8894181282062928, 0.8266096100995073, 0.8887437317216671, 0.7864754042670632, 0.8304034418246317, 0.851851214957365, 0.8553247661299167, 0.878765826225497, 0.8621884275212157, 0.8317203868655482, 0.880295845023209, 0.8640019858707195, 0.8709190483911753, 0.9021976421890603, 0.855637796657605]
n40_v_avg_values_3 = [0.12099987683350565, 0.03451369793293734, 0.05272527166530482, 0.008536823498114804, 0.05477727486256142, 0.002795508581561988, 0.05066207559138588, 0.08718662548563474, 0.12562853554552875, 0.2185593633417123, 0.1707269652487898, 0.14377935618266732, 0.29702408999674573, 0.15115394990304334, 0.17189771046585, 0.32028259728960085, 0.3309671443852924, 0.6005239902385916, 0.44316533983760936, 0.39861001354550224, 0.582774455210813, 0.6404340086330538, 0.7450817739198451, 0.7402154600007435, 0.7747771196400484, 0.699785955992233, 0.7268065972762713, 0.6516425186433491, 0.8131071927600316, 0.7015234025139104, 0.809507012798103, 0.7678058813644187, 0.8308812956234483, 0.8641243267902413, 0.8097855068659113, 0.9089316889382508, 0.9049232399487579, 0.7591123818996883, 0.7973271451416846, 0.8668157012848406, 0.8041758534987209, 0.8424724766308538, 0.8592866855784856, 0.8901655833022968, 0.8149524126312954, 0.9174279412808247, 0.8818451257967002, 0.9012671586641131, 0.8158268557932008, 0.9166958187917835, 0.8303739663021654]
n40_v_avg_values = [(n40_v_avg_values_1[i] + n40_v_avg_values_2[i] + n40_v_avg_values_3[i]) / 3 for i in range(len(n40_v_avg_values_1))]


n10_v_avg_values = gaussian_filter1d(n10_v_avg_values, sigma=2)
n20_v_avg_values = gaussian_filter1d(n20_v_avg_values, sigma=2)
n30_v_avg_values = gaussian_filter1d(n30_v_avg_values, sigma=2)
n40_v_avg_values = gaussian_filter1d(n40_v_avg_values, sigma=2)
plt.plot(r_values, n10_v_avg_values, label='n=0.1 pi')
plt.plot(r_values, n20_v_avg_values, label='n=0.2 pi')
plt.plot(r_values, n30_v_avg_values, label='n=0.3 pi')
plt.plot(r_values, n40_v_avg_values, label='n=0.4 pi')


plt.xlabel('Radius')
plt.ylabel('Average Velocity')
plt.title('Average Velocity vs Radius')
plt.grid(True)
plt.legend()
plt.show()
