# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.4.2
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x05:\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15  as T\x0a\
\x0aT.ProgressBar {\
\x0a    id: control\
\x0a\x0a    implicitWi\
dth: Math.max(im\
plicitBackground\
Width + leftInse\
t + rightInset,\x0a\
                \
            impl\
icitContentWidth\
 + leftPadding +\
 rightPadding)\x0a \
   implicitHeigh\
t: Math.max(impl\
icitBackgroundHe\
ight + topInset \
+ bottomInset,\x0a \
                \
            impl\
icitContentHeigh\
t + topPadding +\
 bottomPadding)\x0a\
\x0a    property in\
t orientation: Q\
t.Horizontal\x0a   \
 padding: 2\x0a\x0a   \
 QtObject {\x0a    \
    id: orient\x0a \
       property \
bool vertical: c\
ontrol.orientati\
on == Qt.Vertica\
l\x0a        proper\
ty bool horizont\
al: control.orie\
ntation == Qt.Ho\
rizontal\x0a    }\x0a\x0a\
    contentItem:\
 Item {\x0a        \
Rectangle {\x0a    \
        x: 2\x0a   \
         y: (par\
ent.height - hei\
ght)/2\x0a         \
   width: contro\
l.position * (pa\
rent.width - 4)\x0a\
            heig\
ht: Math.min(wid\
th, parent.heigh\
t - 4)\x0a\x0a        \
    radius: Math\
.max(width, heig\
ht)\x0a            \
color: control.p\
alette.button\x0a  \
      }\x0a    }\x0a\x0a \
   background: R\
ectangle {\x0a     \
   implicitWidth\
: orient.horizon\
tal ? 200 : 18\x0a \
       implicitH\
eight: orient.ve\
rtical ? 200 : 1\
8\x0a\x0a        color\
: 'transparent'\x0a\
        radius: \
width\x0a\x0a        b\
order {\x0a        \
    color: contr\
ol.palette.butto\
n\x0a            wi\
dth: 2\x0a        }\
\x0a    }\x0a}\x0a\
\x00\x00\x03%\
\x00\
\x00\x0b\x92x\xda\xddV\xddO\xdb0\x10\x7f\xcf_q\
\xeb\x03\xb4\x83\xa4\xa5\x88i\x0aB\x08:m\xab\xc4\xa6\
2\xba1i\xda\x83\x9b\xb8\x8dEbG\xce\x85\xb6B\
\xfd\xdf\xe7|8\x1fM\x0a\x9d\xc4^\x96\x97\xf6>\xfc\
\xf3\xdd\xef\xceg\xf7\xfb0\x12\xe1Z\xb2\x85\x87\xd0\x1d\
\xf5`8\x18\x0e!\x0a\xa4e\xf4\xfbp7\xf9\xf0\xd3\
\xbca\x0e\xe5\x115\xc7.\xe5\xc8\xe6\x8cJ\x1bn>\
Mn\xccSk`\x0a\xee\xaf\x13O\x0f1\xb4\xfb\xfd\
\xc8\x0cLi1i\x18,\x08\x85D\xb8\xc5\xdb\x989\
\x0f0\xb4N\xce\xb6t\xd6\x94\x06\xa1O\x90F\xa9\x15\
H\x04S\xc3\x98Z#\x8f:\x0f\xd7b\x05O\x06\xa8\
\x8f\xb968\x82\xa3\x14\xbe\x91)\xd4*\xe60\xbcg\
.z6|!\xe8Y\x01Yu\xb5\xfe\x9a8\x0f\x0b\
)b\xee\xa6\x1ep\x04>\x9d\xe3X\xa5\x80\xea\x7f\x9a\
i*\x1c\xa7h\xbb>\x8d6R[\xab\xbc\xabP\x13\
\xe2\xba\x8c/4X.\xf6j\xc1}\xa6\x89\xe9\xd9\xe8\
2\x17\x85\x82\x22\xd4\xd1\xcd\x04\xa2\x08\xf6\x08o;\xbe\
*X\x19_\x06\x97\xcb{\x02\x8e\xb9\xcb\x1c\x82B\xbe\
\x02\xa4\x86\xb2\xbc\x97\xb12\xfe\xc2L\xb0\xe1]*F\
!qr\xd1\xa8!\xda\xf0\x8d:H\xf8\xc2\xa7y\x9f\
\xb4\xb4\xc6\xf0\xaca\xd1uQ\xa6\xc2\xb6*\x1a\xccB\
\xbaB\xb8\xdc\xce\xaa\xab\xcd\x01\x93RH\xea6]\xd2\
O\xbb-\xd3f1A\xffj}\xb5]\xc0~\x16\xa2\
\xd2g\xbd\xa6k\x8b\x97\xa2\xb3\x08\x93<\x12\xe6\x93\x99\
O\xef\xab\x81\xf4\xa0\x0f\xc32\xebu%\xebjQ\x9a\
(y#\x98\x90Uq\x0bG\x12\x97\xc5\x91\x0d\x15B\
\x1d\xe1'\x15:DI\xb8\xaa\xa0T\xfdyXZg\
B\xbaTV\xaaVY\xa2\xf7~dQL\xfc\x8f\xc2\
\x89#\xb8,\xb4!\xf1)\x22\xb5<\x15\x86\x9f\xc6d\
7l\xb3X\xf5\x14\xafa/\xf3n(\x94\x9b2\x98\
\xb6.\xd2S\x87\xcd\xc4\xaa\xa6T\x8d\xd2\xcd\xd2\xa9\x97\
8c\xa4\xea\xb9.=\xbdg\xd9k\xc9}+\x93\x9a\
\xab&\xfb\xb4\xae\x8e0\x19\xa3\xf6\xafFK\xdd%\x86\
\xad\xd4\x0aZ<\xca\xcb]\x9dd\xeaf\xee\x17\x17\x17\
jFgs\x98\xba\xadk'R\x84T\xe2z\xe4)\
\xf2\xd4\x00\x7f\xda9\x08\x90\xc8\x05\xc5\x162[*\xa4\
c)\xe7\x86\xa6\xf9\xfd\xce\xa5^~\xa0\x9bk\x0b\xe2\
\xdb\x17o\x1a\xda\xcd\xf1\xab\xf2\xf7\x9d;\x7f\xc3`\x8d\
\xa9sM\xc9\xe0\xbc\xc8p\xf0\xefC\x9e\x10\x89\x8c\xf8\
\xfe\xfa\xff\xa8}\xfft\xdf\xca\xd74\xbf\xeb\x87+\x9d\
b\x0c\x99\xe0\xea\xe05\x8f\xd8\xb40\xef`b.E\
`C\xe7m\xa7\xd5\x8ab\xb7\xedk\x1c\xcc\xa8\xbc\xe2\
, \x19>\x84\x19\xf7L\x1dv\xe8\xa4\x04\x1d\xe7,\
t\xce\xc1\x8de\xeag\xc3\xc9`\xb0G\x96u}>\
\x14\x9d\xec=1F\xaa\x82\x9e&\xd7a\x99U\xe5\xba\
i!\x1d\x0e\x0e\xe0M\xf3\xa6\xdcY\xd9\xa3\xc2\x92\xdf\
\xf2j\x9a\x0f\xcak\xa5rW\xee\xd8\xec\xd5\xf6zL\
(u\x88\x7f\xa5.\x15\x1e\xa8\xec\xb3\xcc\xadT\xfe1\
R\x0a*\x0b\xe7\xe4\x89P\x7f0\x14\xa6\xb9\xe0\x15S\
\x22\x19/\xcc\xf8\xa5\x0aT,\xa7\x1adcl\x8c?\
\x9a\xed+\xc9\
\x00\x00\x07\xc9\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15 as T\x0ai\
mport SnowWhite \
1.0\x0a\x0aT.RadioButt\
on {\x0a    id: con\
trol\x0a\x0a    implic\
itWidth: Math.ma\
x(implicitBackgr\
oundWidth + left\
Inset + rightIns\
et,\x0a            \
                \
implicitContentW\
idth + leftPaddi\
ng + rightPaddin\
g)\x0a    implicitH\
eight: Math.max(\
implicitBackgrou\
ndHeight + topIn\
set + bottomInse\
t,\x0a             \
               i\
mplicitContentHe\
ight + topPaddin\
g + bottomPaddin\
g,\x0a             \
               i\
mplicitIndicator\
Height + topPadd\
ing + bottomPadd\
ing)\x0a\x0a    paddin\
g: 6\x0a    spacing\
: 6\x0a\x0a    indicat\
or: Rectangle {\x0a\
        implicit\
Width:  25\x0a     \
   implicitHeigh\
t: 25\x0a\x0a        x\
: control.text ?\
\x0a               \
(control.mirrore\
d ?\x0a            \
        control.\
width - width - \
control.rightPad\
ding :\x0a         \
           contr\
ol.leftPadding) \
:\x0a              \
 control.leftPad\
ding + (control.\
availableWidth -\
 width) / 2\x0a\x0a   \
     y: control.\
topPadding + (co\
ntrol.availableH\
eight - height) \
/ 2\x0a\x0a        rad\
ius: width\x0a\x0a    \
    color: 'tran\
sparent'\x0a\x0a      \
  border {\x0a     \
       color: co\
ntrol.visualFocu\
s ? control.pale\
tte.highlight : \
control.palette.\
button\x0a         \
   width: 2\x0a    \
    }\x0a\x0a        R\
ectangle {\x0a     \
       id: ibox\x0a\
            x: (\
parent.width - w\
idth) / 2\x0a      \
      y: (parent\
.height - height\
) / 2\x0a\x0a         \
   width: contro\
l.checked ? pare\
nt.width - 8 : 0\
\x0a            hei\
ght: width\x0a\x0a    \
        color: p\
alette.button\x0a\x0a \
           radiu\
s: width\x0a\x0a      \
      Behavior o\
n width {\x0a      \
          Number\
Animation { dura\
tion: 100 }\x0a    \
        }\x0a      \
  }\x0a    }\x0a\x0a    c\
ontentItem: Text\
 {\x0a        leftP\
adding: control.\
indicator && !co\
ntrol.mirrored ?\
 control.indicat\
or.width + contr\
ol.spacing : 0\x0a \
       rightPadd\
ing: control.ind\
icator && contro\
l.mirrored ? con\
trol.indicator.w\
idth + control.s\
pacing : 0\x0a     \
   verticalAlign\
ment: Text.Align\
VCenter\x0a        \
color: palette.w\
indowText\x0a      \
  text: control.\
text\x0a        fon\
t: control.font\x0a\
    }\x0a}\x0a\
\x00\x00\x08\x5c\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15 as T\x0a\x0a\
T.TextField {\x0a  \
  id: control\x0a\x0a \
   implicitWidth\
: implicitBackgr\
oundWidth + left\
Inset + rightIns\
et\x0a             \
      || Math.ma\
x(contentWidth, \
placeholder.impl\
icitWidth) + lef\
tPadding + right\
Padding\x0a    impl\
icitHeight: Math\
.max(implicitBac\
kgroundHeight + \
topInset + botto\
mInset,\x0a        \
                \
     contentHeig\
ht + topPadding \
+ bottomPadding,\
\x0a               \
              pl\
aceholder.implic\
itHeight + topPa\
dding + bottomPa\
dding)\x0a\x0a    padd\
ing: 6\x0a    leftP\
adding: padding \
+ 4\x0a\x0a    color: \
control.palette.\
windowText\x0a    s\
electionColor: c\
ontrol.palette.h\
ighlight\x0a    sel\
ectedTextColor: \
control.palette.\
highlightedText\x0a\
    placeholderT\
extColor: contro\
l.palette.text\x0a \
   verticalAlign\
ment: TextInput.\
AlignVCenter\x0a\x0a  \
  Text {\x0a       \
 id: placeholder\
\x0a        x: cont\
rol.leftPadding\x0a\
        y: contr\
ol.topPadding\x0a  \
      width: con\
trol.width - (co\
ntrol.leftPaddin\
g  + control.rig\
htPadding)\x0a     \
   height: contr\
ol.height  - (co\
ntrol.topPadding\
   + control.bot\
tomPadding)\x0a\x0a   \
     text: contr\
ol.placeholderTe\
xt\x0a        font:\
 control.font\x0a\x0a \
       color: co\
ntrol.placeholde\
rTextColor\x0a\x0a    \
    verticalAlig\
nment: control.v\
erticalAlignment\
\x0a        visible\
: !control.lengt\
h && !control.pr\
eeditText && (!c\
ontrol.activeFoc\
us || control.ho\
rizontalAlignmen\
t !== Qt.AlignHC\
enter)\x0a        e\
lide: Text.Elide\
Right\x0a        re\
nderType: contro\
l.renderType\x0a   \
 }\x0a\x0a    backgrou\
nd: Rectangle {\x0a\
        implicit\
Width: 200\x0a     \
   implicitHeigh\
t: 40\x0a\x0a        o\
pacity: control.\
activeFocus ? 1 \
: 0.5\x0a        co\
lor: Qt.lighter(\
palette.window, \
palette.window.h\
slLightness * 2)\
\x0a\x0a        border\
.color: Qt.light\
er(palette.butto\
n, 0.5 + palette\
.window.hslLight\
ness)\x0a        bo\
rder.width: 0.5\x0a\
\x0a        Behavio\
r on opacity { N\
umberAnimation {\
 duration: 100 }\
 }\x0a\x0a        Rect\
angle {\x0a        \
    height: pare\
nt.height\x0a      \
      width: con\
trol.activeFocus\
 ? 3 : 1\x0a\x0a      \
      color: con\
trol.enabled ? c\
ontrol.palette.b\
utton : '#000000\
55'\x0a\x0a           \
 Behavior on wid\
th { NumberAnima\
tion { duration:\
 100 } }\x0a       \
 }\x0a    }\x0a}\x0a\
\x00\x00\x04\xb9\
\x00\
\x00\x0f\xf6x\xda\xb5W[o\xdb6\x14~\xd7\xaf`\
\xfaP\xd8[-\xdbJ\xd3m\x1a\x82 \x97v1\x10\
oic\xb4\x03\xb6=\xd0\x12\x13\x13\x95D\x81\xa2|\
Y\x9a\xff\xbeCR\xa2HII\x1cl\x13\xd0\x86<\
7\x1e~<7\x8f\xc7\xe8\x9c\xe5;N\xefV\x02\x0d\
\xce\x87(\x98\x04\x01*R\xee{\xe31\xba\xb9\xbe\xf8\
}tE#\x92\x15d4\x8bI&\xe8-%<D\
W\xbf\x5c_\x8d\x0e\xfd\xc9\x88e\xc9NJ\xae\x84\xc8\
\xc3\xf1\xb8\x18\xa5#\xeeS\xeey4\xcd\x19\x17\xe8\xa3\
\xf8X\xd2\xe8+\x0a\xfc\xe9Q\x8b\xe6\x9f\xb3Lp\x96\
\x14\xbd\xcc/4\x8b\xd9\xa6\x97\xb5 i\x9e`A\xb4\
\x22B\xb8@\x0b\xcf[\x80\xbdt\xc9\xce\xd8\x16\xdd{\
\x08>\x1a\x87(\xd2Gx\x9a\x00j4\xa2\xe2\x0b\x8d\
\xc5*Ds,V~\x8a\xb7\x83\x9a~\x86\xa3\xafw\
\x9c\x95Y\xac$\xd0\xf7(!\xb7b\x06w\x17\xb0V\
\x10\xa9\xcd\x1be\xed\xb1\xaf\xb6&o\x07\x80\xd9\xa6\xae\
q\x1c\xd3\xec\xae6Vm\x87\x8es\x97D\xb2\x9e\xf4\
N\x8b\x80\x15\xc1\xf2\xda\xbb%\x13\x82\xa5/w\xcf\xb6\
\xd5\xb8\xa7\xadU\xfb\xfd\xec\xcd\xb2\x98FX0\xbe\x87\
E}c\x0b\x91\x10\x1d\x81\xcc\xe0\xa0z.?\xa5\x9c\
3Nb\xf4\xed\x1b:\xa0\xb5ew\xe7\xafiA\x97\
\x09A'h\x82B\xd4\xd07\x15\xe2E\x8e#s\x98\
\x0dxu\xda\xffwX\xb5\x81st\xe0\xc5$!w\
\x10\xb0!\x9a\x09\x92^T\xbb*L\xe5\xb7\xd1\x11y\
E\x0b\xf1\x99\x92\x0d\x9c\x06\xff)\xa2\x11\x11d+L\
<\xfbr\xf7\x89)\x7f\x06\xa7\x9c\xe3\x9dO\x0b\xf5\xb7\
\xb9\x15\x83S\x87\xc0W\x8b\x0b,\xf0\x1fm\xe5\xbf\xe0\
&\x8a\xdb\xe5\x0ck\x96T4>\xe48!B\x10\xdf\
\xf5\xa5\xa6.Kx\xe2l\x01\xbc\x8e\xc2\x0a\xd0O\xe4\
\x0b\x90x\xd1\xab\xdb\x120\x06VlM\xf8\xfb\x0c\x03\
\xf4M6\xfb6\xd53\xb2K\x93 !\xfaD\x22\x81\
\xb3\xbb\xc4\x06Y\x85\x01\x8eiY\xc8\x87\xb1\xa9\x11K\
\x18\x7f\xecB\x8e$\x93/+v\x8dlTr\x0ei\
\x04\xd1O\xb6\xe8\xf8\xf8X\x86\x06\xac x\x94\x93\x10\
U'h\x0a`N\xfc\x1f\x1cCK\xc6cR\x85O\
\x88 \xbaJ\x9c|`QY\x80|\x00\xf2\xd3>\xe9\
'\xfdT\xb89Zgd\x85\xd7\x14B\x99e\xb5\xe3\
\xe8\x1e\xfdZ\xa6K\xc2O3\x9abA\x81s\x8f\xe2\
\x92\xab%\x9c:\x99\xa0\x07\xf4\xe0\x9ay\x0cK\xf9m\
Cxc\x09@\x95\x08\xdf\xc1E\x7f\xeaH\x01^\x83\
Jl\xa5\xab\xc3\x08\xe9\xc5p\x1ct\xa4+L\x8e~\
\xaed\xd4\xb2~87)\xf6z@'\xa0\xea\xaf\xca\
\xe7\xe7\x1e\xd2\xd1{\xf0\xdcU\x85\x93)\x06!\x92G\
Y(m\x1b\xf3\xa6\xc8\x9cX^\xea\xe2\xd8\x08\xe15\
\xa6\x89\x8c\xea\xbai\xd4\x8c\xaa\xa0\x00\xe5\xadg\x81j\
\xd2\xd6\xae\xb4\x83\x8e\xb5\xcb\xc71\xaf\xb0v:\xa3\xf7\
rTuAx\xf5g\x19\x04\xef\xa6\xaf\x0c\xf9\x164\
\xfd\x9cnIrC\xff\x06\xac\xa7\x81\xcbZ\xb2\x04r\
U\xf0\x92x\x9d\x04#:\xbdM\xfa\x1c\xda\x90G\xba\
y\xc9j\x0a\xa0\xfb\xd2\x97\x0f\x94$\xb1\x85\xbd\xd3]\
\x0ez\x9ea\xaa\xd2\xec\xd0(\xb8\x1db\x0f\x85\xba\xfb\
\xaa\xf8\xb4\xfa\xaf]]\xdcJIb*\xb0\xee\x226\
IEM#\x15\xd3\x02\xc6\x9b\x9d\x9b\xcf\xa4]\x03k\
[F\x02\x97\x82\xddD\xc0J\x9e\x10\xe2\x04\xc7\xbf\xc1\
\xc8fA\xd2\x91\xa1Y^\x8a9\x11+\x16_\xd2L\
\x14\x8d\xb96\xc7\xa8\xacqBc\x9d\x02\xb5\xac!\x19\
\xa1\x02\xfa^$\xcevsV\x16V\xe2i\xb2\xbcm\
\xc5\xf2\x9c i\x04\xe5\xee\xb9\xd8\xdc\xa8\xa9\xd1\x89M\
m\x1f\xca\xdby\xbf\x8ai=-\x0d\xdd\x89\x9eSj\
\xf5+(\xf9\x02\x8aAr\x0a\xcc,%\xd2}\xc9\xf7\
\xd5\xfe\xf39\x10\x08\x7fY\xc7\xea\x14\xaa:1^\xbf\
\xee\xc6\x15\xd0\xcc\xbb\xde\xc2\x88\xbcO\x97\xd3\x90\xf5w\
\xb9\xaahc\xc0oMt{\xea;\xf6DV}\x95\
\xa5\xefz\xbbm\xf0\x1f\xb5\xa5\xde\xf2\xfb\x1c\x88\xad\xa9\
\x7f\xfav\xd2a\xd537\xb0\xbc\x0e\xee\x0e\xa0\xb2\xb1\
\x9b<e\x9bf8\xe8\x0e\x16\xfb\x0d\x15\x9d\x81BZ\
U\x80\xfe(\xab\x8doy\xf4\xefp\xab\xd0\xcaY^\
\xe6\xb2f^\xcb\x85\x05\x93\xe5\x82n\x13v\x9d3e\
\xb1\xd39j\x1d\xb7/\xaf\x9c\x1f14\x1bX\x05\xdb\
wQ\x7fcL\xe8_|\xcd\x84\xb0\x83\x7f5o7\
\x84\xce\x16x\x16\xb8V\x03\xa8\xc7\xe6V\xe6D\x09\xcd\
[\xdd\xa5\xef\xd1#\xfb\x87\x90#\xa9\x06`\xebe\xaa\
\xb9}.\xc9\x8e\xa0\x99\xf7\xdd@\xb7G\x0a\x0b\xdd\xa6\
t\xcc:#\x86a\xceaz\xbc0\x0f9q\x84\x16\
\xbe\xae\xf3\xb3\xe6\xd7IUvB\xd4\xe2@8t\xd3\
\xe6\xc1\xfb\x07\xf6\xd0\xe6-\
\x00\x00\x00\x9f\
i\
mport QtQuick 2.\
15\x0aimport QtQuic\
k.Templates 2.15\
 as T\x0a\x0aT.Label {\
\x0a    id: control\
\x0a\x0a    color: con\
trol.palette.win\
dowText\x0a    link\
Color: control.p\
alette.link\x0a}\x0a\
\x00\x00\x07\xe4\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15 as T\x0a\x0a\
T.Tumbler {\x0a    \
id: control\x0a\x0a   \
 implicitWidth: \
Math.max(implici\
tBackgroundWidth\
 + leftInset + r\
ightInset,\x0a     \
                \
       implicitC\
ontentWidth + le\
ftPadding + righ\
tPadding)\x0a    im\
plicitHeight: Ma\
th.max(implicitB\
ackgroundHeight \
+ topInset + bot\
tomInset,\x0a      \
                \
       implicitC\
ontentHeight + t\
opPadding + bott\
omPadding)\x0a\x0a    \
font.pixelSize: \
12\x0a    palette.t\
ext: \x22gray\x22\x0a\x0a   \
 delegate: Text \
{\x0a        text: \
modelData\x0a      \
  color: control\
.visualFocus ? c\
ontrol.palette.h\
ighlightedText :\
 control.palette\
.buttonText\x0a    \
    font: contro\
l.font\x0a        o\
pacity: 0.4 + Ma\
th.max(0, 1 - Ma\
th.abs(Tumbler.d\
isplacement)) * \
0.6\x0a        hori\
zontalAlignment:\
 Text.AlignHCent\
er\x0a        verti\
calAlignment: Te\
xt.AlignVCenter\x0a\
    }\x0a\x0a    conte\
ntItem: PathView\
 {\x0a        id: p\
athview\x0a        \
preferredHighlig\
htBegin: 0.5\x0a   \
     preferredHi\
ghlightEnd: 0.5\x0a\
        highligh\
tRangeMode: Path\
View.StrictlyEnf\
orceRange\x0a      \
  implicitWidth:\
 60\x0a        impl\
icitHeight: 80\x0a \
       clip: tru\
e\x0a        model:\
 control.model\x0a \
       delegate:\
 control.delegat\
e\x0a        pathIt\
emCount: control\
.visibleItemCoun\
t\x0a        path: \
Path {\x0a         \
   startX: contr\
ol.availableWidt\
h / 2\x0a          \
  startY: 0\x0a    \
        PathLine\
 {\x0a             \
   x: control.av\
ailableWidth / 2\
\x0a               \
 y: control.avai\
lableHeight\x0a    \
        }\x0a      \
  }\x0a    }\x0a\x0a    b\
ackground: Recta\
ngle {\x0a        i\
mplicitWidth: 60\
\x0a        implici\
tHeight: 80\x0a    \
    radius: 5\x0a  \
      color: con\
trol.palette.but\
ton\x0a\x0a        Rec\
tangle {\x0a       \
     y: (parent.\
height - height)\
/2\x0a            x\
: (parent.width \
- width)/2\x0a     \
       width: pa\
rent.width * 0.7\
\x0a            hei\
ght: control.cur\
rentItem.height\x0a\
            radi\
us: 3\x0a          \
  opacity: Math.\
abs(pathview.off\
set % 1 - 0.5) *\
 2\x0a            b\
order.width: 1\x0a \
           borde\
r.color: control\
.palette.window\x0a\
            colo\
r: 'transparent'\
\x0a        }\x0a    }\
\x0a}\x0a\
\x00\x00\x01#\
\x00\
\x00\x04\x17x\xda\xcd\x92MK\xc3@\x10\x86\xef\xfb+\
\x86\x9e\xf4\x90M\x1a\x11a{\x92ZD(\xda\xd2 \
^\xb7\x9bm;\xb4\xfb\xc1\xec\x04\x0d\xd2\xffn\x9a*\
\x88\xd7z\xc8\xdc\xf6\x9d\x17\xf6\xe1a\xf2\x1c\xa6!\xb6\
\x84\xdb\x1d\xc3\xd5\xf4\x1a\xca\xa2,!9\x92\x22\xcfa\
\xb5xx\xcb\xe6h\xacO6{\xaa\xadg\xdc\xa0%\
\x05\xf3\xc7\xc5<\xbb\x91E\x16\xfc\xa1=5w\xccQ\
\xe5y\xca\x5cF\x12I\x08t1\x10\xc3\x92\x97\x0d\x9a\
=\x94r|\xfb'\x93\x95u\xf1\xa0\xd9\xa6~\x0b\xa0\
\x13TBTr\xc5\xda\xec_\xd1\xbe\xc3\xa7\x80n\xb0\
V`\x82g\x0a\x07\xd1\x07\xb1I\xbb\x99\xe7\x13HE\
\xda'd\x0c\xfe\xbb|\x9a\xe7\xc6\xad-\xdd{t\xfa\
\xbc\x81H!Z\xe2V\xc1(Dm\x90\xdb\xd1\x046\
\x14\x9c\x82b\x02\x1c\x14\x8c'P7\xd4\xf7\x15\xdc\x15\
]juB\xbf\x95\xdcF\xab`v~\xbc4<m\
\xd6h\xe0\xd8\x7fv\xfc\xc5\xf3\x81\xfc\x1f8\xe33N\
q\x09N\x88\xbd\x1d\x18\x8a\x9e\x8e\xa7\xb3\x03\x03\xd1C\
\xb6\xbb:c\x07\xa5\xe8\x87i\x18\x9a\x8e\xe2\x0b\xc7\xd7\
J\x1d\
\x00\x00\x06C\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0a\x0aimport \
QtQuick 2.15\x0aimp\
ort QtQuick.Temp\
lates 2.15 as T\x0a\
\x0aT.Slider {\x0a    \
id: control\x0a\x0a   \
 implicitWidth: \
Math.max(implici\
tBackgroundWidth\
 + leftInset + r\
ightInset,\x0a     \
                \
       implicitH\
andleWidth + lef\
tPadding + right\
Padding)\x0a    imp\
licitHeight: Mat\
h.max(implicitBa\
ckgroundHeight +\
 topInset + bott\
omInset,\x0a       \
                \
      implicitHa\
ndleHeight + top\
Padding + bottom\
Padding)\x0a    pad\
ding: 6\x0a\x0a    han\
dle: Rectangle {\
\x0a        x: cont\
rol.leftPadding \
+ (control.horiz\
ontal ? control.\
visualPosition *\
 (control.availa\
bleWidth - width\
) : (control.ava\
ilableWidth - wi\
dth) / 2)\x0a      \
  y: control.top\
Padding + (contr\
ol.horizontal ? \
(control.availab\
leHeight - heigh\
t) / 2 : control\
.visualPosition \
* (control.avail\
ableHeight - hei\
ght))\x0a\x0a        i\
mplicitWidth: 20\
\x0a        implici\
tHeight: 20\x0a\x0a   \
     color: cont\
rol.palette.butt\
on\x0a        radiu\
s: width\x0a\x0a      \
  border {\x0a     \
       color: vi\
sualFocus ? cont\
rol.palette.high\
light : control.\
palette.window\x0a \
           width\
: 2\x0a        }\x0a\x0a \
       Behavior \
on border.width \
{ NumberAnimatio\
n{ duration: 100\
} }\x0a    }\x0a\x0a    b\
ackground: Recta\
ngle {\x0a        x\
: (control.width\
  - width) / 2\x0a \
       y: (contr\
ol.height - heig\
ht) / 2\x0a\x0a       \
 implicitWidth: \
control.horizont\
al ? 200 : 2\x0a   \
     implicitHei\
ght: control.hor\
izontal ? 2 : 20\
0\x0a\x0a        width\
: control.horizo\
ntal ? control.a\
vailableWidth : \
implicitWidth\x0a  \
      height: co\
ntrol.horizontal\
 ? implicitHeigh\
t : control.avai\
lableHeight\x0a\x0a   \
     radius: wid\
th\x0a\x0a        colo\
r: control.palet\
te.button\x0a    }\x0a\
}\x0a\
\x00\x00\x0aZ\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0a\x0aimport \
QtQuick 2.15\x0aimp\
ort QtQuick.Temp\
lates 2.15 as T\x0a\
\x0aT.SpinBox {\x0a   \
 id: control\x0a\x0a  \
  implicitWidth:\
 Math.max(implic\
itBackgroundWidt\
h + leftInset + \
rightInset,\x0a    \
                \
        contentI\
tem.implicitWidt\
h + 2 * padding \
+\x0a              \
              up\
.implicitIndicat\
orWidth +\x0a      \
                \
      down.impli\
citIndicatorWidt\
h)\x0a    implicitH\
eight: Math.max(\
implicitContentH\
eight + topPaddi\
ng + bottomPaddi\
ng,\x0a            \
                \
 implicitBackgro\
undHeight,\x0a     \
                \
        up.impli\
citIndicatorHeig\
ht,\x0a            \
                \
 down.implicitIn\
dicatorHeight)\x0a\x0a\
    padding: 6\x0a \
   leftPadding: \
padding + (contr\
ol.mirrored ? (u\
p.indicator ? up\
.indicator.width\
 : 0) : (down.in\
dicator ? down.i\
ndicator.width :\
 0))\x0a    rightPa\
dding: padding +\
 (control.mirror\
ed ? (down.indic\
ator ? down.indi\
cator.width : 0)\
 : (up.indicator\
 ? up.indicator.\
width : 0))\x0a    \
font.bold: true\x0a\
\x0a    component I\
ndicator: Text {\
\x0a        width: \
30; height: pare\
nt.height\x0a\x0a     \
   font.pointSiz\
e: 10\x0a        fo\
nt.bold: true\x0a\x0a \
       color: co\
ntrol.palette.bu\
tton\x0a        hor\
izontalAlignment\
: Text.AlignHCen\
ter\x0a        vert\
icalAlignment: T\
ext.AlignVCenter\
\x0a    }\x0a\x0a    vali\
dator: IntValida\
tor {\x0a        lo\
cale: control.lo\
cale.name\x0a      \
  bottom: Math.m\
in(control.from,\
 control.to)\x0a   \
     top: Math.m\
ax(control.from,\
 control.to)\x0a   \
 }\x0a\x0a    contentI\
tem: TextInput {\
\x0a        text: c\
ontrol.displayTe\
xt\x0a\x0a        font\
: control.font\x0a \
       color: co\
ntrol.palette.bu\
tton\x0a        sel\
ectionColor: con\
trol.palette.hig\
hlight\x0a        s\
electedTextColor\
: control.palett\
e.highlightedTex\
t\x0a        horizo\
ntalAlignment: T\
ext.AlignHCenter\
\x0a        vertica\
lAlignment: Text\
.AlignVCenter\x0a\x0a \
       readOnly:\
 !control.editab\
le\x0a        valid\
ator: control.va\
lidator\x0a        \
inputMethodHints\
: control.inputM\
ethodHints\x0a\x0a    \
    Rectangle {\x0a\
            y: p\
arent.height - h\
eight\x0a          \
  width: parent.\
width\x0a          \
  height: parent\
.readOnly ? 0 : \
1\x0a            co\
lor: control.pal\
ette.button\x0a    \
    }\x0a    }\x0a\x0a   \
 up.indicator: I\
ndicator {\x0a     \
   x: control.mi\
rrored ? 0 : par\
ent.width - widt\
h\x0a        text: \
\x22+\x22;\x0a        opa\
city: !enabled |\
| control.up.pre\
ssed ? 0.4 : 1\x0a \
   }\x0a\x0a    down.i\
ndicator: Indica\
tor {\x0a        x:\
 control.mirrore\
d ? parent.width\
 - width : 0\x0a   \
     text: \x22-\x22;\x0a\
        opacity:\
 !enabled || con\
trol.down.presse\
d ? 0.4 : 1\x0a    \
}\x0a\x0a\x0a    backgrou\
nd: Rectangle {\x0a\
        id: back\
ground\x0a        i\
mplicitWidth: 80\
\x0a        implici\
tHeight: 30\x0a\x0a   \
     radius: 5\x0a \
       color: 't\
ransparent'\x0a    \
    border.width\
: 2\x0a        bord\
er.color: contro\
l.palette.button\
\x0a    }\x0a}\x0a\
\x00\x00\x02\x88\
\x00\
\x00\x08\xe8x\xda\xd5TM\x8f\xda0\x10\xbd#\xf1\x1f\
\xa67h7\x0e\xa4j\x0f\xb9T*U\xbb+Q\x09\
v\x91\xda\xabI\x0c\xb1\xd6\xc4\x91\xed\x10h\xb5\xff\xbd\
\x8e\x13c\x12\x12\x96=6B\xc2\xf6\xbcy\xf3\xe17\
\xf6}\x98\xf1\xec(\xe86Q0\x9a\x8d!\x98\x04\x01\
\xc8\x9d@\xc3\x81\xef\xc3\xd3\xe2\xdbooN#\x92J\
\xe2=\xc4$UtC\x89\x08a\xfec1\xf7>\xa2\
\x89\xc7Sv4\xd0D\xa9,\xf4}\xe9\xed<\x81\xa8\
\x18\x0e\x86\x03\xba\xcb\xb8P\xb0T\xcb\x9cF\xcf\x10\xa0\
\xe9\xa7\xf6!Z\x91]\xc6\xb0\x22\xd2\x98\x01KX]\
`f<U\x823\x09'\xccr9+\x03\xac\xd0#\
N\xb7\xe4\x89\xd1\x98\x08\xf8;\x1c\x80\xfeh\x1cBT\
y\x94\x18s\xa4c\xd0\x88\xaa_4VI\x08?\xb1\
J\xd0\x0e\x1fF\xf6\xfc+\x8e\x9e\xb7\x82\xe7il\x10\
\xf0\x01\x18\xd9\xa8\x07]\xb4\xd2k\xd3\x1c\xb3\xb9\xab\xe8\
\xfa\xbe\x0d\x15R!Kz\x8f\xd3\x98\x91s\xc2\x05\x8e\
c\x9an-e\xbd}\x85T\x12]L\xfcf\xd6q\
\xb3\xf2{R\xda\xae\x96^A4\x8d\xe2\x99-}\xcd\
\x95\xe2\xbb[j\xef,\xfe\x9c\xd2\xa5Y\x91\xdeV}\
w\xf97\xf0\xd6\xf5g\xd5.\x84\xcfV\x0b\x11\xd7\xe2\
J\xb5\x92\xa1\xe2\xd2b~$\x91\xd2:b\xc4J\xc8\
x\x0a\x9e\x11\xa1\x8e \x08f\xb0\xcf\xb8\x0ca\xe2\xcc\
\x87\x93\xc8P\xf3\x12F\xf68\xe1\x82\xfe\xd1k\xed\xfd\
\xc5\xf8\xc3{g\xc4{L\x19^\xdb\x9b\xf4\xa0(\xff\
\xc7\x10\xbe\x0e\xf1!\x18\xbb<\x8e.\x8fF3F\xef\
\xde\x96G\xddR\x0f\x12\xb3\xe8\xce\xe4\x02T\xe5\xe2\xb2\
i\x0dZ0\xb94Y%\x966g\x158\xa6\xb9\xee\
\xb0\xa9\xb1\xa4u\xa65\x17g\xd3m\xbf\x883.\x5c\
\xed\x19fD)\x82\x0a\x9a\xc6\xbchB\x8b:\x19w\
\xfaR-_l\x06\x95v\x13\xa3\x87\xd0\xea\xe2<b\
u\xfd6X\x05\xdfS\x99c\xb6\xe0\x92*\xcaS\x87\
meV\x813A\xa4$\xb1\xbe\x81\xa5B\xac\xec\x00\
\x11\xa3v\xf2\xeb\x5c\x0b8\xbd\x83)\x9a\x96\xfd\xef6\
\xb7\x1b\x83\xeax8RtO\xbe\xf3(\x97:J\xdb\
7\xd1!MX\xb8\xde\xb3SK\xea\xb9\xbb\xb9'5\
\xfe\xc6\xa6\xd4\xe8\xff\xae+\xeb\xd3k\xd9\xf3j\x1c\xce\
\xc6\xa6\xb8\x98\xdb\xc6\xd8\xba\x87\xa2c\xaa\xae\x0c\xd5i\
\xb0\xf7\xfay\xa2\x91\x19\xeb`2\x81\x86\xc2\xdb\xd3v\
\xcd\xc7y\x15\xfd\x11z^\xa5\xb0\x99\x9d\xa3J\xfa\x03\
\xf7=+a+\xeb\xde\xf7\xa1WV]\x9a\xd0w\xa7\
\x7f\xff\x00\xe9\xeb\xbb\x8a\
\x00\x00\x08\xd3\
/\
/ Copyright (C) \
2022 smr.\x0d\x0a// SP\
DX-License-Ident\
ifier: LGPL-3.0-\
only\x0d\x0a// http://\
s-m-r.ir\x0d\x0a\x0d\x0a\x0d\x0aim\
port QtQuick 2.1\
5\x0d\x0aimport QtQuic\
k.Templates 2.15\
 as T\x0d\x0a\x0d\x0aT.Switc\
h {\x0d\x0a    id: con\
trol\x0d\x0a\x0d\x0a    impl\
icitWidth: Math.\
max(implicitBack\
groundWidth + le\
ftInset + rightI\
nset,\x0d\x0a         \
                \
   implicitConte\
ntWidth + leftPa\
dding + rightPad\
ding)\x0d\x0a    impli\
citHeight: Math.\
max(implicitBack\
groundHeight + t\
opInset + bottom\
Inset,\x0d\x0a        \
                \
     implicitCon\
tentHeight + top\
Padding + bottom\
Padding,\x0d\x0a      \
                \
       implicitI\
ndicatorHeight +\
 topPadding + bo\
ttomPadding)\x0d\x0a\x0d\x0a\
    padding: 6\x0d\x0a\
    spacing: 6\x0d\x0a\
\x0d\x0a    indicator:\
 Rectangle {\x0d\x0a  \
      implicitWi\
dth: 50\x0d\x0a       \
 implicitHeight:\
 25\x0d\x0a\x0d\x0a        x\
: control.text ?\
\x0d\x0a              \
 (control.mirror\
ed ?\x0d\x0a          \
          contro\
l.width - width \
- control.rightP\
adding :\x0d\x0a      \
              co\
ntrol.leftPaddin\
g) :\x0d\x0a          \
     control.lef\
tPadding + (cont\
rol.availableWid\
th - width) / 2\x0d\
\x0a\x0d\x0a        y: co\
ntrol.topPadding\
 + (control.avai\
lableHeight - he\
ight) / 2\x0d\x0a\x0d\x0a   \
     color: 'tra\
nsparent'\x0d\x0a\x0d\x0a   \
     radius: 5\x0d\x0a\
\x0d\x0a        border\
 {\x0d\x0a            \
color: control.v\
isualFocus ? con\
trol.palette.hig\
hlight : control\
.palette.button\x0d\
\x0a            wid\
th: 2\x0d\x0a        }\
\x0d\x0a\x0d\x0a        Rect\
angle {\x0d\x0a       \
     id: ibox\x0d\x0a \
           x: Ma\
th.min(Math.max(\
y, control.visua\
lPosition * pare\
nt.width - heigh\
t/2), parent.wid\
th - height - y)\
\x0d\x0a            y:\
 4\x0d\x0a\x0d\x0a          \
  color: control\
.palette.button\x0d\
\x0a\x0d\x0a            w\
idth: {\x0d\x0a       \
         let pos\
 = Math.abs(0.5 \
- (x-y)/(parent.\
implicitWidth - \
height - 2 * y))\
;\x0d\x0a             \
   height + 8 - \
pos * 8 * 2\x0d\x0a   \
         }\x0d\x0a    \
        height: \
control.indicato\
r.height - 8\x0d\x0a\x0d\x0a\
            radi\
us: 3\x0d\x0a\x0d\x0a       \
     Behavior on\
 x {\x0d\x0a          \
      enabled: !\
control.down\x0d\x0a  \
              Nu\
mberAnimation{ d\
uration: 200 }\x0d\x0a\
            }\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a\x0d\x0a    contentIt\
em: Text {\x0d\x0a    \
    leftPadding:\
 control.indicat\
or && !control.m\
irrored ? contro\
l.indicator.widt\
h + control.spac\
ing : 0\x0d\x0a       \
 rightPadding: c\
ontrol.indicator\
 &&  control.mir\
rored ? control.\
indicator.width \
+ control.spacin\
g : 0\x0d\x0a        v\
erticalAlignment\
: Text.AlignVCen\
ter\x0d\x0a        tex\
t: control.text\x0d\
\x0a        font: c\
ontrol.font\x0d\x0a   \
     color: cont\
rol.palette.wind\
owText\x0d\x0a    }\x0d\x0a}\
\x0d\x0a\
\x00\x00\x02\x84\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15  as T\x0a\
\x0aT.Frame {\x0a    i\
d: control\x0a\x0a    \
implicitWidth: M\
ath.max(implicit\
BackgroundWidth \
+ leftInset + ri\
ghtInset,\x0a      \
                \
      contentWid\
th + leftPadding\
 + rightPadding)\
\x0a    implicitHei\
ght: Math.max(im\
plicitBackground\
Height + topInse\
t + bottomInset,\
\x0a               \
              co\
ntentHeight + to\
pPadding + botto\
mPadding)\x0a\x0a    p\
adding: 6\x0a\x0a    b\
ackground: Recta\
ngle {\x0a        c\
olor: 'transpare\
nt'\x0a        radi\
us: 3\x0a        bo\
rder.width: 1\x0a  \
      border.col\
or: control.pale\
tte.button\x0a    }\
\x0a}\x0a\
\x00\x00\x03\x86\
m\
odule SnowWhite\x0a\
typeinfo snowwhi\
te.qmltypes\x0a\x0aScr\
ipt             \
    1.0 script.j\
s\x0a\x0asingleton Sno\
wWhite    1.0 Sn\
owWhite.qml\x0a\x0aDas\
hedRing         \
    1.0 base/Das\
hedRing.qml\x0a\x0aBut\
ton             \
    1.0 Button.q\
ml\x0aBusyIndicator\
          1.0 Bu\
syIndicator.qml\x0a\
CheckBox        \
       1.0 Check\
Box.qml\x0aLabel   \
               1\
.0 Label.qml\x0aPro\
gressBar        \
    1.0 Progress\
Bar.qml\x0aRadioBut\
ton            1\
.0 RadioButton.q\
ml\x0aRangeSlider  \
          1.0 Ra\
ngeSlider.qml\x0aSl\
ider            \
     1.0 Slider.\
qml\x0aSpinBox     \
           1.0 S\
pinBox.qml\x0aSwitc\
h               \
  1.0 Switch.qml\
\x0aTextArea       \
        1.0 Text\
Area.qml\x0aTextFie\
ld              \
1.0 TextField.qm\
l\x0aTumbler       \
         1.0 Tum\
bler.qml\x0aHorizon\
talSeprator     \
1.0 HorizontalSe\
prator.qml\x0aSplit\
View            \
  1.0 SplitView.\
qml\x0aFrame       \
           1.0 F\
rame.qml\x0aDial   \
                \
1.0 Dial.qml\x0aCom\
boBox           \
    1.0 ComboBox\
.qml\x0a\
\x00\x00\x03[\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0apragma S\
ingleton\x0aimport \
QtQuick 2.15\x0a\x0aQt\
Object {\x0a    /**\
\x0a      *\x0a      *\
/\x0a    function b\
lend(color1, col\
or2) {\x0a        l\
et color = color\
1;\x0a        color\
.r = (color1.r +\
 color2.r) / 2;\x0a\
        color.g \
= (color1.g + co\
lor2.g) / 2;\x0a   \
     color.b = (\
color1.b + color\
2.b) / 2;\x0a      \
  color.b = (col\
or1.a + color2.a\
) / 2;\x0a        r\
eturn color;\x0a   \
 }\x0a\x0a    function\
 setAlpha(color,\
 alpha) {\x0a      \
  color.a = alph\
a;\x0a        retur\
n color;\x0a    }\x0a\x0a\
    function cla\
mp(x, a, b) {\x0a  \
      return Mat\
h.min(Math.max(x\
, a), b);\x0a    }\x0a\
\x0a    function re\
map(value, low1,\
 high1, low2, hi\
gh2) {\x0a        r\
eturn low2 + (hi\
gh2 - low2) * (v\
alue - low1) / (\
high1 - low1);\x0a \
   }\x0a\x0a    functi\
on invertColor(c\
olor) {\x0a        \
return Qt.rgba(1\
.0 - color.r, 1.\
0 - color.g, 1.0\
 - color.b, 1.0)\
;\x0a    }\x0a}\x0a\
\x00\x00\x06_\
i\
mport QtQuick 2.\
15\x0d\x0aimport QtQui\
ck.Templates 2.1\
5 as T\x0d\x0a\x0d\x0aT.Busy\
Indicator {\x0d\x0a   \
 id: control\x0d\x0a\x0d\x0a\
    implicitWidt\
h: Math.max(impl\
icitBackgroundWi\
dth + leftInset \
+ rightInset,\x0d\x0a \
                \
               i\
mplicitContentWi\
dth + leftPaddin\
g + rightPadding\
)\x0d\x0a    implicitH\
eight: Math.max(\
implicitBackgrou\
ndHeight + topIn\
set + bottomInse\
t,\x0d\x0a            \
                \
 implicitContent\
Height + topPadd\
ing + bottomPadd\
ing)\x0d\x0a\x0d\x0a    visi\
ble: running\x0d\x0a  \
  running: false\
\x0d\x0a    padding: 6\
\x0d\x0a\x0d\x0a    contentI\
tem: ShaderEffec\
t {\x0d\x0a        id:\
 effect\x0d\x0a\x0d\x0a     \
   property real\
 strokeWidth: 0.\
06\x0d\x0a        prop\
erty real sweepA\
ngle: .5\x0d\x0a      \
  property color\
 color: control.\
palette.button\x0d\x0a\
\x0d\x0a        fragme\
ntShader: \x22\x0d\x0a   \
         varying\
 highp vec2 qt_T\
exCoord0;\x0d\x0a     \
       uniform h\
ighp float qt_Op\
acity;\x0d\x0a        \
    uniform high\
p float sweepAng\
le;\x0d\x0a           \
 uniform highp f\
loat strokeWidth\
;\x0d\x0a            u\
niform highp flo\
at width;\x0d\x0a     \
       uniform h\
ighp vec4 color;\
\x0d\x0a\x0d\x0a            \
void main() {\x0d\x0a \
               h\
ighp vec2 coord \
= qt_TexCoord0 -\
 vec2(0.5);\x0d\x0a   \
             hig\
hp float ring = \
smoothstep(0.0, \
0.5/width, -abs(\
length(coord) - \
0.5 + strokeWidt\
h) + strokeWidth\
);\x0d\x0a            \
    gl_FragColor\
 = color * ring;\
\x0d\x0a              \
  gl_FragColor *\
= smoothstep(0.0\
, 0.5/width, -at\
an(coord.x, coor\
d.y) / 6.2831 - \
0.48 + sweepAngl\
e);\x0d\x0a           \
 }\x22\x0d\x0a    }\x0d\x0a\x0d\x0a  \
  Timer {\x0d\x0a     \
   property real\
 seed: 0\x0d\x0a      \
  running: contr\
ol.running\x0d\x0a    \
    repeat: true\
; interval: 25 /\
/ Almost 40Hz\x0d\x0a \
       onTrigger\
ed: {\x0d\x0a         \
   effect.rotati\
on += 8\x0d\x0a       \
     effect.swee\
pAngle = 0.5 + M\
ath.sin(seed+=0.\
05) / 3\x0d\x0a       \
 }\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x08\x87\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15 as T\x0a\x0a\
T.TextArea {\x0a   \
 id: control\x0a\x0a  \
  implicitWidth:\
 Math.max(conten\
tWidth + leftPad\
ding + rightPadd\
ing,\x0a           \
                \
 implicitBackgro\
undWidth + leftI\
nset + rightInse\
t,\x0a             \
               p\
laceholder.impli\
citWidth + leftP\
adding + rightPa\
dding)\x0a    impli\
citHeight: Math.\
max(contentHeigh\
t + topPadding +\
 bottomPadding,\x0a\
                \
             imp\
licitBackgroundH\
eight + topInset\
 + bottomInset,\x0a\
                \
             pla\
ceholder.implici\
tHeight + topPad\
ding + bottomPad\
ding)\x0a\x0a    paddi\
ng: 6\x0a    leftPa\
dding: padding +\
 4\x0a\x0a    color: c\
ontrol.palette.w\
indowText\x0a    pl\
aceholderTextCol\
or: palette.mid\x0a\
    selectionCol\
or: control.pale\
tte.highlight\x0a  \
  selectedTextCo\
lor: control.pal\
ette.highlighted\
Text\x0a\x0a    Text {\
\x0a        id: pla\
ceholder\x0a       \
 x: control.left\
Padding\x0a        \
y: control.topPa\
dding\x0a        wi\
dth: control.wid\
th    - (control\
.leftPadding  + \
control.rightPad\
ding)\x0a        he\
ight: control.he\
ight  - (control\
.topPadding   + \
control.bottomPa\
dding)\x0a\x0a        \
text: control.pl\
aceholderText\x0a  \
      font: cont\
rol.font\x0a\x0a      \
  color: control\
.placeholderText\
Color\x0a\x0a        v\
erticalAlignment\
: control.vertic\
alAlignment\x0a    \
    visible: !co\
ntrol.length && \
!control.preedit\
Text && (!contro\
l.activeFocus ||\
 control.horizon\
talAlignment !==\
 Qt.AlignHCenter\
)\x0a        elide:\
 Text.ElideRight\
\x0a        renderT\
ype: control.ren\
derType\x0a    }\x0a\x0a \
   background: R\
ectangle {\x0a     \
   implicitWidth\
: 200\x0a        im\
plicitHeight: 40\
\x0a\x0a        opacit\
y: control.activ\
eFocus ? 1 : 0.5\
\x0a        color: \
Qt.lighter(palet\
te.window, palet\
te.window.hslLig\
htness * 2)\x0a\x0a   \
     border.colo\
r: Qt.lighter(pa\
lette.button, 0.\
5 + palette.wind\
ow.hslLightness)\
\x0a        border.\
width: 0.5\x0a\x0a    \
    Behavior on \
opacity { Number\
Animation { dura\
tion: 100 } }\x0a\x0a \
       Rectangle\
 {\x0a            y\
: parent.height \
- height\x0a       \
     height: con\
trol.activeFocus\
 ? 3 : 1\x0a       \
     width: pare\
nt.width\x0a       \
     color: cont\
rol.enabled ? co\
ntrol.palette.bu\
tton : '#aaa'\x0a\x0a \
           Behav\
ior on height { \
NumberAnimation \
{ duration: 100 \
} }\x0a        }\x0a  \
  }\x0a}\x0a\
\x00\x00\x0d\x04\
/\
/ Copyright (C) \
2022 smr.\x0d\x0a// SP\
DX-License-Ident\
ifier: LGPL-3.0-\
only\x0d\x0a// http://\
s-m-r.ir\x0d\x0a\x0d\x0aimpo\
rt QtQuick 2.15\x0d\
\x0aimport QtQuick.\
Templates 2.15 a\
s T\x0d\x0aimport QtQu\
ick.Controls 2.1\
5\x0d\x0aimport SnowWh\
ite 1.0\x0d\x0a\x0d\x0aT.But\
ton {\x0d\x0a    id: c\
ontrol\x0d\x0a\x0d\x0a    im\
plicitWidth: Mat\
h.max(implicitBa\
ckgroundWidth + \
leftInset + righ\
tInset,\x0d\x0a       \
                \
         implici\
tContentWidth + \
leftPadding + ri\
ghtPadding)\x0d\x0a   \
 implicitHeight:\
 Math.max(implic\
itBackgroundHeig\
ht + topInset + \
bottomInset,\x0d\x0a  \
                \
              im\
plicitContentHei\
ght + topPadding\
 + bottomPadding\
)\x0d\x0a\x0d\x0a    propert\
y alias radius: \
background.radiu\
s\x0d\x0a\x0d\x0a    padding\
: 6\x0d\x0a    spacing\
: 6\x0d\x0a\x0d\x0a    icon.\
width: 24\x0d\x0a    i\
con.height: 24\x0d\x0a\
    icon.color: \
palette.buttonTe\
xt\x0d\x0a\x0d\x0a    displa\
y: AbstractButto\
n.TextOnly\x0d\x0a\x0d\x0a  \
  contentItem: I\
tem {\x0d\x0a        G\
rid {\x0d\x0a         \
   anchors.cente\
rIn: parent\x0d\x0a   \
         spacing\
: control.displa\
y == AbstractBut\
ton.TextOnly ||\x0d\
\x0a               \
      control.di\
splay == Abstrac\
tButton.IconOnly\
 ? 0 : control.s\
pacing\x0d\x0a\x0d\x0a      \
      flow: cont\
rol.display == A\
bstractButton.Te\
xtUnderIcon ?\x0d\x0a \
                \
     Grid.TopToB\
ottom : Grid.Lef\
tToRight\x0d\x0a      \
      layoutDire\
ction: control.m\
irrored ? Qt.Rig\
htToLeft : Qt.Le\
ftToRight\x0d\x0a\x0d\x0a   \
         opacity\
: control.down |\
| control.checke\
d ? 0.8 : 1.0\x0d\x0a\x0d\
\x0a            Ima\
ge {\x0d\x0a          \
      visible: c\
ontrol.display !\
= AbstractButton\
.TextOnly\x0d\x0a     \
           sourc\
e: control.icon.\
source\x0d\x0a        \
        width: c\
ontrol.icon.widt\
h\x0d\x0a             \
   height: contr\
ol.icon.height\x0d\x0a\
                \
cache: control.i\
con.cache\x0d\x0a     \
       }\x0d\x0a\x0d\x0a    \
        Text {\x0d\x0a\
                \
visible: control\
.display != Abst\
ractButton.IconO\
nly\x0d\x0a           \
     text: contr\
ol.text\x0d\x0a       \
         font: c\
ontrol.font\x0d\x0a   \
             col\
or: !control.ena\
bled ? 'gray' :\x0d\
\x0a               \
     control.hig\
hlighted ? palet\
te.highlightedTe\
xt :\x0d\x0a          \
                \
                \
palette.buttonTe\
xt\x0d\x0a            \
    horizontalAl\
ignment: Text.Al\
ignHCenter\x0d\x0a    \
        }\x0d\x0a     \
   }\x0d\x0a    }\x0d\x0a\x0d\x0a \
   background: R\
ectangle {\x0d\x0a    \
    id: backgrou\
nd\x0d\x0a        visi\
ble: control.ena\
bled\x0d\x0a\x0d\x0a        \
implicitWidth: 4\
5\x0d\x0a        impli\
citHeight: 45\x0d\x0a\x0d\
\x0a        radius:\
 width * 0.2\x0d\x0a  \
      opacity: c\
ontrol.flat ? 0.\
5 : 1.0\x0d\x0a\x0d\x0a     \
   color: {\x0d\x0a   \
         const  \
_color =  contro\
l.highlighted ? \
palette.highligh\
t : palette.butt\
on\x0d\x0a            \
control.down ? Q\
t.lighter(_color\
, 1.1) : _color\x0d\
\x0a        }\x0d\x0a\x0d\x0a  \
      border {\x0d\x0a\
            widt\
h: control.visua\
lFocus ? 1 :0\x0d\x0a \
           color\
: palette.window\
Text\x0d\x0a        }\x0d\
\x0a\x0d\x0a        Behav\
ior on border.wi\
dth { NumberAnim\
ation { duration\
: 75 } }\x0d\x0a\x0d\x0a    \
    Rectangle {\x0d\
\x0a            x: \
(parent.width - \
width)/2\x0d\x0a      \
      y: (parent\
.height - height\
)/2\x0d\x0a           \
 radius: parent.\
radius - 0.05\x0d\x0a \
           visib\
le: control.chec\
ked\x0d\x0a           \
 color: 'transpa\
rent'\x0d\x0a         \
   border {\x0d\x0a   \
             col\
or: palette.butt\
onText\x0d\x0a        \
        width: 1\
\x0d\x0a            }\x0d\
\x0a\x0d\x0a            N\
umberAnimation o\
n width {\x0d\x0a     \
           runni\
ng: control.chec\
ked\x0d\x0a           \
     from: contr\
ol.background.wi\
dth\x0d\x0a           \
     to: control\
.background.widt\
h - 5\x0d\x0a         \
   }\x0d\x0a\x0d\x0a        \
    NumberAnimat\
ion on height {\x0d\
\x0a               \
 running: contro\
l.checked\x0d\x0a     \
           from:\
 control.backgro\
und.height\x0d\x0a    \
            to: \
control.backgrou\
nd.height - 5\x0d\x0a \
           }\x0d\x0a  \
      }\x0d\x0a    }\x0d\x0a\
}\x0d\x0a\
\x00\x00\x02\xf4\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15  as T\x0a\
\x0aT.SplitView {\x0a \
   id: control\x0a \
   implicitWidth\
: Math.max(impli\
citBackgroundWid\
th + leftInset +\
 rightInset,\x0a   \
                \
         implici\
tContentWidth + \
leftPadding + ri\
ghtPadding)\x0a    \
implicitHeight: \
Math.max(implici\
tBackgroundHeigh\
t + topInset + b\
ottomInset,\x0a    \
                \
         implici\
tContentHeight +\
 topPadding + bo\
ttomPadding)\x0a\x0a  \
  handle: Rectan\
gle {\x0a        im\
plicitWidth: con\
trol.orientation\
 === Qt.Horizont\
al ? 4 : control\
.width\x0a        i\
mplicitHeight: c\
ontrol.orientati\
on === Qt.Horizo\
ntal ? control.h\
eight : 4\x0a      \
  color: control\
.enabled ? contr\
ol.palette.butto\
n : '#aaa'\x0a    }\
\x0a}\x0a\
\x00\x00\x00X\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\
\x00\x00\x06\xd8\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Templ\
ates 2.15 as T\x0ai\
mport QtQuick.Co\
ntrols 2.15\x0aimpo\
rt SnowWhite 1.0\
\x0a\x0aT.Dial {\x0a    i\
d: control\x0a    p\
roperty alias do\
ttedRing: dotted\
Ring\x0a\x0a    implic\
itWidth: Math.ma\
x(implicitBackgr\
oundWidth + left\
Inset + rightIns\
et,\x0a            \
                \
implicitContentW\
idth + leftPaddi\
ng + rightPaddin\
g)\x0a    implicitH\
eight: Math.max(\
implicitBackgrou\
ndHeight + topIn\
set + bottomInse\
t,\x0a             \
                \
implicitContentH\
eight + topPaddi\
ng + bottomPaddi\
ng)\x0a\x0a    backgro\
und: Item {\x0a    \
    implicitWidt\
h: 184\x0a        i\
mplicitHeight: 1\
84\x0a\x0a        clip\
: true\x0a\x0a        \
Rectangle {\x0a    \
        x: (cont\
rol.availableWid\
th - width)/2\x0a  \
          y: (co\
ntrol.availableH\
eight - height)/\
2\x0a\x0a            i\
mplicitWidth: pa\
rent.width - 20\x0a\
            impl\
icitHeight: pare\
nt.width - 20\x0a\x0a \
           radiu\
s: width\x0a\x0a      \
      border.col\
or: 'transparent\
'\x0a\x0a            b\
order.width: 1\x0a \
           color\
: control.palett\
e.button\x0a       \
 }\x0a\x0a        Dash\
edRing {\x0a       \
     id: dottedR\
ing\x0a\x0a           \
 x: (control.ava\
ilableWidth - wi\
dth)/2\x0a         \
   y: (control.a\
vailableHeight -\
 height)/2\x0a\x0a    \
        implicit\
Width: parent.wi\
dth - 5\x0a        \
    implicitHeig\
ht: parent.width\
 - 5\x0a\x0a          \
  borderWidth: 2\
\x0a            das\
hWidth: 2\x0a      \
      dashCount:\
 25\x0a            \
palette.base: co\
ntrol.palette.bu\
tton\x0a        }\x0a \
   }\x0a\x0a    handle\
: Item {\x0a       \
 width: control.\
width\x0a        he\
ight: control.he\
ight\x0a\x0a        ro\
tation: control.\
angle * 1.07\x0a\x0a  \
      Rectangle \
{\x0a            x:\
 (parent.width -\
 width)/2\x0a      \
      y: 12\x0a    \
        width: 2\
; height: 20\x0a   \
         radius:\
 width\x0a         \
   color: contro\
l.palette.button\
Text\x0a        }\x0a \
   }\x0a}\x0a\
\x00\x00\x06*\
/\
/ Copyright (C) \
2022 smr.\x0a// SPD\
X-License-Identi\
fier: LGPL-3.0-o\
nly\x0a// http://s-\
m-r.ir\x0a\x0aimport Q\
tQuick 2.15\x0aimpo\
rt QtQuick.Contr\
ols 2.15\x0a\x0aContro\
l {\x0a    id: cont\
rol\x0a\x0a    propert\
y real dashCount\
: 2\x0a    property\
 real dashWidth:\
 2\x0a    property \
real borderWidth\
: 2\x0a\x0a    ShaderE\
ffect {\x0a        \
    id: effect\x0a \
           width\
: parent.width;\x0a\
            heig\
ht: width;\x0a     \
       readonly \
property real co\
unt: 360 / contr\
ol.dashCount\x0a   \
         readonl\
y property real \
dashWidth: contr\
ol.dashWidth / 2\
\x0a            rea\
donly property r\
eal borderWidth:\
 control.borderW\
idth / width / 2\
\x0a            rea\
donly property r\
eal smoothstp: 0\
.5 / width\x0a     \
       readonly \
property color c\
olor: control.pa\
lette.base;\x0a\x0a   \
         fragmen\
tShader: \x22\x0a     \
           varyi\
ng highp vec2 qt\
_TexCoord0;\x0a    \
            unif\
orm highp float \
qt_Opacity;\x0a    \
            unif\
orm highp float \
count;\x0a         \
       uniform h\
ighp float dashW\
idth;\x0a          \
      uniform hi\
ghp float border\
Width;\x0a         \
       uniform h\
ighp float smoot\
hstp;\x0a          \
      uniform hi\
ghp vec4 color;\x0a\
\x0a               \
 void main() {\x0a \
                \
   highp vec2 no\
rmal = qt_TexCoo\
rd0 - vec2(0.5);\
\x0a               \
     gl_FragColo\
r = color;\x0a     \
               h\
ighp float ticks\
 = smoothstep(0.\
0, 20 * smoothst\
p / count, -abs(\
fract(atan(norma\
l.x, normal.y) *\
 57.2958 / count\
) - 0.5) + dashW\
idth / count);\x0a \
                \
   highp float r\
ing = smoothstep\
(0.0, smoothstp,\
 -abs(length(nor\
mal) - 0.5 + bor\
derWidth) + bord\
erWidth);\x0a      \
              gl\
_FragColor = gl_\
FragColor * ring\
 * ticks;\x0a      \
          }\x22\x0a   \
     }\x0a}\x0a\
"

qt_resource_name = b"\
\x00\x09\
\x06\xcdD\x05\
\x00S\
\x00n\x00o\x00w\x00W\x00h\x00i\x00t\x00e\
\x00\x0f\
\x03U\x9e\x9c\
\x00P\
\x00r\x00o\x00g\x00r\x00e\x00s\x00s\x00B\x00a\x00r\x00.\x00q\x00m\x00l\
\x00\x0c\
\x00V'\xdc\
\x00C\
\x00h\x00e\x00c\x00k\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x0f\
\x0dg\x10\xbc\
\x00R\
\x00a\x00d\x00i\x00o\x00B\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\x00\x0d\
\x01\xb8P\x9c\
\x00T\
\x00e\x00x\x00t\x00F\x00i\x00e\x00l\x00d\x00.\x00q\x00m\x00l\
\x00\x0c\
\x00'&\x5c\
\x00C\
\x00o\x00m\x00b\x00o\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x09\
\x08\xbf\xf4\xdc\
\x00L\
\x00a\x00b\x00e\x00l\x00.\x00q\x00m\x00l\
\x00\x0b\
\x02r\xd3\x1c\
\x00T\
\x00u\x00m\x00b\x00l\x00e\x00r\x00.\x00q\x00m\x00l\
\x00\x0d\
\x0a\x89\x18\xdc\
\x00S\
\x00t\x00a\x00c\x00k\x00V\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
\x00\x0a\
\x0a\xce\x15\xdc\
\x00S\
\x00l\x00i\x00d\x00e\x00r\x00.\x00q\x00m\x00l\
\x00\x0b\
\x09\xdf\xb8|\
\x00S\
\x00p\x00i\x00n\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x0f\
\x03q\xf3\xdc\
\x00R\
\x00a\x00n\x00g\x00e\x00S\x00l\x00i\x00d\x00e\x00r\x00.\x00q\x00m\x00l\
\x00\x0a\
\x0a\x90\x0c<\
\x00S\
\x00w\x00i\x00t\x00c\x00h\x00.\x00q\x00m\x00l\
\x00\x09\
\x088\xcf<\
\x00F\
\x00r\x00a\x00m\x00e\x00.\x00q\x00m\x00l\
\x00\x06\
\x07\x84+\x02\
\x00q\
\x00m\x00l\x00d\x00i\x00r\
\x00\x04\
\x00\x06\x88\x95\
\x00b\
\x00a\x00s\x00e\
\x00\x0d\
\x04\x0d\xce\xbc\
\x00S\
\x00n\x00o\x00w\x00W\x00h\x00i\x00t\x00e\x00.\x00q\x00m\x00l\
\x00\x11\
\x0a\xd7\x90\xbc\
\x00B\
\x00u\x00s\x00y\x00I\x00n\x00d\x00i\x00c\x00a\x00t\x00o\x00r\x00.\x00q\x00m\x00l\
\
\x00\x0c\
\x03\xed\xa9<\
\x00T\
\x00e\x00x\x00t\x00A\x00r\x00e\x00a\x00.\x00q\x00m\x00l\
\x00\x0a\
\x0bhq\x5c\
\x00B\
\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\x00\x0d\
\x0b0F\xdc\
\x00S\
\x00p\x00l\x00i\x00t\x00V\x00i\x00e\x00w\x00.\x00q\x00m\x00l\
\x00\x09\
\x09\x07\x86S\
\x00s\
\x00c\x00r\x00i\x00p\x00t\x00.\x00j\x00s\
\x00\x08\
\x0f\x7fa|\
\x00D\
\x00i\x00a\x00l\x00.\x00q\x00m\x00l\
\x00\x0e\
\x01w9\xfc\
\x00D\
\x00a\x00s\x00h\x00e\x00d\x00R\x00i\x00n\x00g\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x16\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x01\xae\x00\x02\x00\x00\x00\x01\x00\x00\x00\x18\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x9e\x00\x01\x00\x00\x00\x01\x00\x00\x18\x94\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x00<\x00\x01\x00\x00\x00\x01\x00\x00\x05>\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x00~\x00\x00\x00\x00\x00\x01\x00\x00\x104\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x00\xd4\x00\x00\x00\x00\x00\x01\x00\x00\x1d\xf4\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x00\x18\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01F\x00\x01\x00\x00\x00\x01\x00\x007\xa8\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x02\x04\x00\x00\x00\x00\x00\x01\x00\x00R\xdf\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01\xbc\x00\x00\x00\x00\x00\x01\x00\x00I\x1d\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01\x9c\x00\x00\x00\x00\x00\x01\x00\x00E\x93\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01\x84\x00\x00\x00\x00\x00\x01\x00\x00C\x0b\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x00\xbc\x00\x00\x00\x00\x00\x01\x00\x00\x1dQ\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x02\x5c\x00\x00\x00\x00\x00\x01\x00\x00kj\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01*\x00\x00\x00\x00\x00\x01\x00\x00-J\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x00\xf0\x00\x01\x00\x00\x00\x01\x00\x00%\xdc\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01j\x00\x00\x00\x00\x00\x01\x00\x00:4\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01\x10\x00\x00\x00\x00\x00\x01\x00\x00'\x03\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x01\xdc\x00\x00\x00\x00\x00\x01\x00\x00L|\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x02<\x00\x00\x00\x00\x00\x01\x00\x00hr\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x02\x22\x00\x00\x00\x00\x00\x01\x00\x00[j\
\x00\x00\x01\x87354\xd5\
\x00\x00\x00Z\x00\x00\x00\x00\x00\x01\x00\x00\x08g\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x02t\x00\x00\x00\x00\x00\x01\x00\x00k\xc6\
\x00\x00\x01\x83\x98G\xd18\
\x00\x00\x02\x8a\x00\x00\x00\x00\x00\x01\x00\x00r\xa2\
\x00\x00\x01\x83\x98G\xd18\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
