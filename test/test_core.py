import unittest
from fuzzy.core import FuzzyPlotly

x_sample_values = ["2013-07",
                   "2013-08",
                   "2013-09",
                   "2013-10",
                   "2013-11",
                   "2013-12",
                   "2014-01",
                   "2014-02",
                   "2014-03",
                   "2014-04",
                   "2014-05",
                   "2014-06",
                   "2014-07",
                   "2014-08",
                   "2014-09",
                   "2014-10",
                   "2014-11",
                   "2014-12",
                   "2015-01",
                   "2015-02",
                   "2015-03",
                   "2015-04",
                   "2015-05",
                   "2015-06",
                   "2015-07",
                   "2015-08",
                   "2015-09",
                   "2015-10",
                   "2015-11",
                   "2015-12",
                   "2016-01",
                   "2016-02",
                   "2016-03",
                   "2016-04",
                   "2016-05",
                   "2016-06",
                   "2016-07",
                   "2016-08",
                   "2016-09",
                   "2016-10",
                   "2016-11",
                   "2016-12",
                   "2017-01",
                   "2017-02",
                   "2017-03",
                   "2017-04",
                   "2017-05",
                   "2017-06",
                   "2017-07",
                   "2017-08",
                   "2017-09",
                   "2017-10",
                   "2017-11",
                   "2017-12",
                   "2018-01",
                   "2018-02",
                   "2018-03",
                   "2018-04",
                   "2018-05",
                   "2018-06",
                   "2018-07",]

y_median = [8.337618963728, 8.279171746205, 8.203023291325001, 8.16982661854, 8.097634166936, 8.008366857893, 8.058186936088001, 7.885838698153, 7.858881576058001, 7.855567493386, 7.820595855792, 7.818122337445001, 7.828704432914, 7.980026665154999, 7.849850895981, 7.79839463565, 7.75388054972, 7.746002782859, 7.668407780941, 7.690985902007999, 7.612645534365, 7.3747395662390005, 7.170755621192, 7.227406558807, 7.171694338855, 6.893654974382, 6.762184038944, 6.598652448781, 6.419642868308999, 6.285297334109, 6.1413396095340005, 6.007282987197, 5.963297915327, 5.9641084307379995, 5.871371751667, 5.713943557774, 5.6704875369000005, 5.586620413797999, 5.550096812713, 5.518101872629, 5.607761950272, 5.6011292164699995, 5.514911517329001, 5.373080972737, 5.288693295291, 5.184773292915, 5.076842783398, 5.099483022613001, 5.087590042512001, 5.116303933252, 5.086588537155, 5.022712701151001, 4.934685111503001, 4.913662261302, 4.885593397848, 4.948802059784, 4.801996126307, 4.840341849932, 4.801265584408, 4.776618718601, 4.7377872479250005]

y_n_95 = [8.141622565273995, 8.083175347750995, 8.007026892870996, 7.973830220085994, 7.9016377684819945, 7.812370459438994, 7.862190537633995, 7.689842299698994, 7.662885177603995, 7.659571094931994, 7.624599457337994, 7.622125938990995, 7.632708034459994, 7.784030266700993, 7.653854497526994, 7.602398237195994, 7.557884151265994, 7.550006384404994, 7.472411382486994, 7.4949895035539935, 7.416649135910994, 7.178743167784995, 6.974759222737994, 7.031410160352994, 6.975697940400994, 6.697658575927994, 6.566187640489995, 6.4026560503269945, 6.223646469854994, 6.089300935654994, 5.945343211079995, 5.811286588742994, 5.767301516872994, 5.768112032283994, 5.675375353212994, 5.517947159319994, 5.474491138445995, 5.3906240153439935, 5.354100414258994, 5.322105474174994, 5.411765551817994, 5.405132818015994, 5.318915118874995, 5.177084574282994, 5.092696896836994, 4.988776894460994, 4.880846384943994, 4.903486624158995, 4.891593644057995, 4.9203075347979945, 4.8905921387009945, 4.826716302696995, 4.738688713048995, 4.717665862847994, 4.689596999393994, 4.752805661329994, 4.6059997278529945, 4.644345451477994, 4.605269185953994, 4.580622320146994, 4.541790849470995]

y_p_95 = [8.533615362182005, 8.475168144659005, 8.399019689779006, 8.365823016994005, 8.293630565390005, 8.204363256347005, 8.254183334542006, 8.081835096607005, 8.054877974512006, 8.051563891840006, 8.016592254246005, 8.014118735899006, 8.024700831368005, 8.176023063609005, 8.045847294435005, 7.994391034104005, 7.949876948174005, 7.941999181313005, 7.864404179395006, 7.886982300462005, 7.808641932819006, 7.5707359646930055, 7.366752019646006, 7.423402957261006, 7.367690737309005, 7.0896513728360055, 6.958180437398006, 6.794648847235006, 6.615639266763004, 6.481293732563005, 6.3373360079880054, 6.203279385651005, 6.159294313781006, 6.160104829192004, 6.0673681501210055, 5.909939956228005, 5.866483935354006, 5.782616812252005, 5.746093211167006, 5.714098271083005, 5.803758348726005, 5.7971256149240045, 5.710907915783006, 5.569077371191005, 5.484689693745006, 5.3807696913690055, 5.272839181852005, 5.2954794210670055, 5.2835864409660065, 5.312300331706005, 5.282584935609005, 5.218709099605006, 5.130681509957006, 5.109658659756006, 5.081589796302005, 5.1447984582380055, 4.997992524761006, 5.036338248386006, 4.997261982862005, 4.972615117055005, 4.9337836463790055]

y_n_60 = [8.253456840370708, 8.195009622847708, 8.11886116796771, 8.085664495182709, 8.013472043578709, 7.924204734535708, 7.974024812730709, 7.801676574795708, 7.774719452700709, 7.771405370028709, 7.736433732434708, 7.733960214087709, 7.744542309556708, 7.895864541797708, 7.765688772623708, 7.714232512292709, 7.669718426362708, 7.661840659501708, 7.5842456575837085, 7.606823778650708, 7.528483411007708, 7.290577442881709, 7.086593497834708, 7.143244435449708, 7.087532215497708, 6.809492851024708, 6.678021915586709, 6.514490325423709, 6.335480744951708, 6.201135210751708, 6.057177486176709, 5.923120863839708, 5.879135791969708, 5.879946307380708, 5.787209628309708, 5.629781434416708, 5.586325413542709, 5.502458290440708, 5.465934689355708, 5.433939749271708, 5.523599826914708, 5.516967093112708, 5.430749393971709, 5.288918849379709, 5.204531171933708, 5.100611169557708, 4.992680660040708, 5.015320899255709, 5.003427919154709, 5.032141809894709, 5.002426413797709, 4.938550577793709, 4.850522988145709, 4.8295001379447084, 4.801431274490708, 4.864639936426708, 4.717834002949709, 4.756179726574708, 4.7171034610507085, 4.6924565952437085, 4.653625124567709]

y_p_60 = [8.421781087085291, 8.363333869562291, 8.287185414682293, 8.253988741897292, 8.181796290293292, 8.092528981250291, 8.142349059445293, 7.9700008215102915, 7.943043699415292, 7.939729616743292, 7.9047579791492915, 7.902284460802292, 7.912866556271291, 8.06418878851229, 7.934013019338291, 7.882556759007292, 7.838042673077291, 7.830164906216291, 7.752569904298292, 7.775148025365291, 7.6968076577222915, 7.458901689596292, 7.254917744549291, 7.311568682164292, 7.255856462212291, 6.977817097739291, 6.846346162301292, 6.682814572138292, 6.503804991666291, 6.3694594574662915, 6.225501732891292, 6.091445110554291, 6.047460038684291, 6.048270554095291, 5.955533875024291, 5.798105681131291, 5.754649660257292, 5.670782537155291, 5.6342589360702915, 5.602263995986291, 5.691924073629291, 5.685291339827291, 5.599073640686292, 5.457243096094292, 5.3728554186482915, 5.268935416272291, 5.161004906755291, 5.183645145970292, 5.171752165869292, 5.200466056609292, 5.170750660512292, 5.106874824508292, 5.018847234860292, 4.997824384659292, 4.9697555212052915, 5.032964183141291, 4.886158249664292, 4.9245039732892915, 4.885427707765292, 4.860780841958292, 4.821949371282292]

y_n_30 = [8.299086917087243, 8.240639699564243, 8.164491244684244, 8.131294571899243, 8.059102120295243, 7.969834811252243, 8.019654889447244, 7.847306651512243, 7.820349529417244, 7.817035446745243, 7.782063809151243, 7.779590290804244, 7.790172386273243, 7.941494618514242, 7.811318849340243, 7.759862589009243, 7.715348503079243, 7.707470736218243, 7.629875734300243, 7.652453855367242, 7.574113487724243, 7.3362075195982435, 7.132223574551243, 7.188874512166243, 7.133162292214243, 6.855122927741243, 6.723651992303243, 6.560120402140243, 6.381110821668242, 6.246765287468243, 6.102807562893243, 5.968750940556243, 5.924765868686243, 5.925576384097242, 5.832839705026243, 5.675411511133243, 5.6319554902592435, 5.548088367157242, 5.511564766072243, 5.479569825988243, 5.569229903631243, 5.5625971698292425, 5.476379470688244, 5.334548926096243, 5.250161248650243, 5.146241246274243, 5.038310736757243, 5.0609509759722435, 5.049057995871244, 5.077771886611243, 5.048056490514243, 4.984180654510244, 4.8961530648622436, 4.875130214661243, 4.847061351207243, 4.910270013143243, 4.763464079666243, 4.801809803291243, 4.762733537767243, 4.738086671960243, 4.6992552012842435]

y_p_30 = [8.376151010368757, 8.317703792845757, 8.241555337965758, 8.208358665180757, 8.136166213576757, 8.046898904533757, 8.096718982728758, 7.924370744793757, 7.897413622698758, 7.894099540026757, 7.859127902432757, 7.856654384085758, 7.867236479554757, 8.018558711795755, 7.888382942621757, 7.836926682290757, 7.792412596360757, 7.784534829499757, 7.706939827581757, 7.729517948648756, 7.651177581005757, 7.4132716128797576, 7.209287667832757, 7.265938605447757, 7.210226385495757, 6.932187021022757, 6.8007160855847575, 6.637184495421757, 6.4581749149497565, 6.323829380749757, 6.1798716561747575, 6.045815033837757, 6.001829961967757, 6.0026404773787565, 5.909903798307757, 5.752475604414757, 5.709019583540758, 5.625152460438756, 5.588628859353757, 5.556633919269757, 5.646293996912757, 5.6396612631107566, 5.553443563969758, 5.411613019377757, 5.327225341931757, 5.223305339555757, 5.115374830038757, 5.138015069253758, 5.126122089152758, 5.154835979892757, 5.125120583795757, 5.061244747791758, 4.973217158143758, 4.952194307942757, 4.924125444488757, 4.987334106424757, 4.840528172947757, 4.878873896572757, 4.839797631048757, 4.815150765241757, 4.7763192945657575]


class CoreFuzzy(unittest.TestCase):
    def setUp(self):
        self.Fuzz01 = FuzzyPlotly(
            x_sample_values, y_median,
            ci95p=y_p_95, ci95n=y_n_95,
            ci60p=y_p_60, ci60n=y_n_60,
            ci30p=y_p_30, ci30n=y_n_30,
            fuzz_size=0.2, fuzz_n=10,
        )
        self.Fuzz02 = FuzzyPlotly(
            x_sample_values, y_median,
            ci95p=y_p_95, ci95n=y_n_95,
            ci60p=y_p_60, ci60n=y_n_60,
            ci30p=y_p_30, ci30n=y_n_30,
            fuzz_size=0.2, fuzz_n=10, color='#00FFFF'
        )
        self.Fuzz03 = FuzzyPlotly(
            x_sample_values, y_median,
            ci95p=y_p_95, ci95n=y_n_95,
            ci60p=y_p_60, ci60n=y_n_60,
            ci30p=y_p_30, ci30n=y_n_30,
            fuzz_size=0.2, fuzz_n=10, color='#800000'
        )

    def test_hex_to_rgb(self):
        color1 = self.Fuzz01.hex_to_rgb(self.Fuzz01.color) # Default color of '#4286f4'
        color2 = self.Fuzz02.hex_to_rgb(self.Fuzz02.color) #'#00FFFF'
        color3 = self.Fuzz03.hex_to_rgb(self.Fuzz03.color) #'#800000'

        self.assertEqual(color1, (66, 134, 244))
        self.assertEqual(color2, (0, 255, 255))
        self.assertEqual(color3, (128, 0, 0))

    def test_create_color(self):
        color_opacity_1 = self.Fuzz01.create_color_opacity()
        color_opacity_2 = self.Fuzz01.create_color_opacity()
        color_opacity_3 = self.Fuzz01.create_color_opacity()

        self.assertEqual(color_opacity_1['w_30'], 1)
        self.assertEqual(color_opacity_1['w_60'], 0.45783120843063346)
        self.assertEqual(color_opacity_1['w_95'], 0.22936163505456264)

        self.assertEqual(color_opacity_2['w_30'], 1)
        self.assertEqual(color_opacity_2['w_60'], 0.45783120843063346)
        self.assertEqual(color_opacity_2['w_95'], 0.22936163505456264)

        self.assertEqual(color_opacity_3['w_30'], 1)
        self.assertEqual(color_opacity_3['w_60'], 0.45783120843063346)
        self.assertEqual(color_opacity_3['w_95'], 0.22936163505456264)

    def test_rgb_to_rgba(self):
        color_hex = self.Fuzz01.color
        color_rgb = self.Fuzz01.hex_to_rgb(color_hex)

        color_opacity = self.Fuzz01.create_color_opacity()

        rgba_30 = self.Fuzz01.rgb_to_rgba_string(color_rgb, color_opacity['w_30'])
        rgba_60 = self.Fuzz01.rgb_to_rgba_string(color_rgb, color_opacity['w_60'])
        rgba_95 = self.Fuzz01.rgb_to_rgba_string(color_rgb, color_opacity['w_95'])

        self.assertEqual(rgba_30, "rgba(66, 134, 244, 1.0)")
        self.assertEqual(rgba_60, "rgba(66, 134, 244, 0.45783120843063346)")
        self.assertEqual(rgba_95, "rgba(66, 134, 244, 0.22936163505456264)")

    # Add assertion
    def test_rbga_to_rgb(self):
        color_hex = self.Fuzz01.color
        color_rgb = self.Fuzz01.hex_to_rgb(color_hex)

        color_opacity = self.Fuzz01.create_color_opacity()

        rgba_30 = color_rgb + (color_opacity['w_30'],)
        rgba_60 = color_rgb + (color_opacity['w_60'],)
        rgba_95 = color_rgb + (color_opacity['w_95'],)

        rgb_30 = self.Fuzz01.rbga_to_rgb(rgba_30)
        rgb_60 = self.Fuzz01.rbga_to_rgb(rgba_60)
        rgb_95 = self.Fuzz01.rbga_to_rgb(rgba_95)

        # print(rgba_30)
        # print(rgba_60)
        # print(rgba_95)
        #
        # print(rgb_30)
        # print(rgb_60)
        # print(rgb_95)

    def test_rgb_to_hex(self):
        color_1_input_hex = self.Fuzz01.color
        color_1_rgb = self.Fuzz01.hex_to_rgb(color_1_input_hex)
        color_1_hex = self.Fuzz01.rgb_to_hex(color_1_rgb)
        print(color_1_hex)

        self.assertEqual(color_1_hex, '#4286f4')
