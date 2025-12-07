
import marshal
import zlib
import base64
import types

# 编码的代码
ENCODED_CODE = b'c${^WTW=dh6vt;~XV+`jL{Np4AXHU=5N>JcC4_)X)GOs`N()VDQLWaVsk`xd?aYqBw$?n5iZ6kX905W+AtXKlPke@XMU~pG&=)vo)^?KsyP7kXo$K#^_RL>o-{U~K04ZGqBZ#0esZ+>VOggO2I!@i`@H(gYH@EIyBf=5<J`sGE)jdIPl8XBXXR1{k<7nMBrH)L~uq7Mafhng=)s15*v>fQ>{)O3W;Z-owE?Q@T3U;5=oqUNp7q0LicSS+?kb9yiN{|=C5m>ft$~R@RujHjLm20a_wr^%kmvQ#z!DKWe0c;;EqzT(2P;vx;IaqCU;o_ysSFXN$?Y;Lu`0%5TYoA>I^v2E4KEJiOb-NxmnnK=f-HW!{aVP2ac2uhSUw$<hj?SDtcYgJawKvz_I`w*m8y>Xf(D*^BMW7q8DFrQ=1UhWQ(iDScKh@Y=VTPwNzH1!l{R>fL*xO^jnram#tqm9+L`kHBpnx0q@F>)Scl7N3W3J44HR<%c?ljr+#$YtbIc8*=ULm`5myW4sP;;Qf2A4F~ZpN_v3b}J`>;NAizDSOdynTs`dB!rnOu#zJ02A{nT3#hPuWf?(6E9<XR{Yw0BW&tVDW)X^Pwp(h(jdSty+tV5VHP^ARj6^gN&pbHa>mf6MUk7Q5K6HM{N$jgHn5uF#GH&y9^^1byi$$3%`i?kR_4PVJp)4wsT7Qp_B#q;8XiZ08sQpOg-J^qCzgrf+ubOsxT*vn>a2aQ?x2D+GA!*K+L!XdU@a|Mbrxxf9tC@xj*k7$-sWCem?o>z4Xe^F8KWw60)D?o$BuR~REQ5&G|zH%Ui^ZM-7&D9xS5wZnVaz?vP>?*4|;*@Q9%0gCea?M24J1q$nER9r`I3-4GX~Gi;ba{p;F;6N8rh%*%eYfhn1pC`W>l4EsYoUdNL8l#r|ofU||?8LLC}M$rQLW3~R><e<wp5hq!=`54tMA?u$?8c(hD?-~)7)4$_%*J^*L#!XpbOqnhqAwV2KD;I9j=3MHmF-~jiVc!D9g7C7vnnmGV$b?j!YaN0~=&-kQ}xfaqoVD=|PtN~1HC)=gWTh0-#TZcZ9@u@>kAsRPKn^E+bzN7F|5N}FR8YQU?lP35M_>ww~1YWUZ8}@8Kd~G#{Y&;<?>=W22ce^MNa-fRXuxu5Yg2w1*iaphBS}vx5fdpn!FJV{f%T6Q)hp`u6B{l5n7iK>k0f)r*Y0AO+w9Lxjo}<MB_@{&B@Nqk(8T>zOyi9!z?0}UGwleg?>kuUz!2s(?@I{h27TnR{iQIp&jxl3`F~`Bkf!{Zw2PODE8FL%jwjcp=I^ihd*c~3%F2s{u90KBaP%31Fi7y<KgcDtCm((AWjD1Q*OS&YuK9c#n^gHrBc>XtZ6R#)u`nA6WD<o`-*g)gfta9pAFjG<c3s8Re^A8Vx{r16+zdii@r?*d3%DF^VmX(=URv>lCdN(LB)e^N<r)}faK~wg0)J;t3Rv7o?Ri(O0okUrSc`)&Tbb!)6kx`vPa~91R>{9HisFiC@<-g>GMNui7Gkw|0%k7&>%P5NL*(k*3!XFZQIz_GG<NcC^9T^00Jq4Yv=*L(t2f<E1jPoyQVHV}`lb%PjKHt@$Xo!C-hLsdg>r>zL@ma9#5PS-{9VJ>S!*pArvnjkB6rXXm{r+oW<5%<TZQv+-6Z&vUpZx=&e*s7'

# 解码和执行
def load_app():
    compressed = base64.b85decode(ENCODED_CODE)
    marshaled = zlib.decompress(compressed)
    code_obj = marshal.loads(marshaled)
    return types.ModuleType("secure_app", code_obj)

if __name__ == "__main__":
    app_module = load_app()
    exec(app_module.__code__)
