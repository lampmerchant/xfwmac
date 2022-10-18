import os
import sys

schemes = {'gtk':       {'c #CCCCFF': 'c #CCCCFF s active_hilight_1',
                         'c #9999CC': 'c #9999CC s active_color_1',
                         'c #666699': 'c #666699 s active_shadow_1',
                         'c #333366': 'c #333366 s active_shadow_1'},
           'gold':      {'c #CCCCFF': 'c #FFCC99',
                         'c #9999CC': 'c #FFCC66',
                         'c #666699': 'c #996666',
                         'c #333366': 'c #996600'},
           'green':     {'c #CCCCFF': 'c #99CC99',
                         'c #9999CC': 'c #669966',
                         'c #666699': 'c #555555',
                         'c #333366': 'c #003300'},
           'turquoise': {'c #CCCCFF': 'c #99FFFF',
                         'c #9999CC': 'c #66CCCC',
                         'c #666699': 'c #669999',
                         'c #333366': 'c #003333'},
           'red':       {'c #CCCCFF': 'c #FFCCCC',
                         'c #9999CC': 'c #FF9999',
                         'c #666699': 'c #996666',
                         'c #333366': 'c #990000'},
           'pink':      {'c #CCCCFF': 'c #FFCCFF',
                         'c #9999CC': 'c #FF99CC',
                         'c #666699': 'c #996699',
                         'c #333366': 'c #990066'},
           'blue':      {'c #CCCCFF': 'c #99CCFF',
                         'c #9999CC': 'c #6699CC',
                         'c #666699': 'c #666699',
                         'c #333366': 'c #003366'},
           'gray':      {'c #CCCCFF': 'c #DDDDDD',
                         'c #9999CC': 'c #BBBBBB',
                         'c #666699': 'c #888888',
                         'c #333366': 'c #333333'}}

def main(argv):
    mypath = os.path.dirname(os.path.realpath(__file__))
    for theme in ('xfwmac7a', 'xfwmac7b'):
        themepath = os.path.join(mypath, theme, 'xfwm4')
        if not os.path.exists(os.path.join(themepath, 'themerc')): continue
        for scheme, colors in schemes.items():
            newthemepath = os.path.join(mypath, '%s-%s' % (theme, scheme), 'xfwm4')
            os.makedirs(newthemepath)
            with open(os.path.join(themepath, 'themerc'), 'rb') as f, open(os.path.join(newthemepath, 'themerc'), 'wb') as g:
                g.write(f.read())
            for filename in os.listdir(themepath):
                if not filename.endswith('.xpm'): continue
                with open(os.path.join(themepath, filename), 'rb') as f, open(os.path.join(newthemepath, filename), 'wb') as g:
                    for line in f:
                        for changefrom, changeto in colors.items():
                            line = line.replace(changefrom, changeto)
                        g.write(line)

if __name__ == '__main__': sys.exit(main(sys.argv))
