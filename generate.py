import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

title_font = {'fontname':'Georgia', 'size':'18', 'color':'black', 'weight':'normal', 'verticalalignment':'bottom'}
sub_font = {'fontname':'Arial', 'size':'10'}

class Page:
    START_X = 0.02
    START_Y = -0.2

    CRATE_SPACING = 0.03
    TEXT_CENTER = 2.5
    TEXT_MARGIN = 0.03

    def __init__(self, names, spacing=0.26):
        self.fig, self.ax = plt.subplots(1,figsize=(8.27,11.69))
        self.ax.set_aspect('equal')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.axis('off')

        for i in range(0, len(names)):
            self.column(self.START_X + i * spacing,
                    self.START_Y, names[i], fles=7, beugel=3)

    def text(self, x, y, content, font=sub_font):
        self.ax.text(x, y, content, font, horizontalalignment='center')

    def circle(self, x, y, size):
        self.ax.add_artist(mpatches.Circle([x,y], radius=size,
            color='black', clip_on=False, fill=False))

    def crate(self, x, y, spacing=0.03, circle_size=0.012, rows=4, columns=6):
        for i in range(0, columns):
            for j in range(0, rows):
                self.circle(x + i * spacing, y + j * spacing, circle_size)

    def column(self, x, y, name, fles=6, beugel=3, spacing=0.14):
        self.text(x + self.TEXT_CENTER * self.CRATE_SPACING, y, name, title_font)
        for i in range(0, fles):
            self.crate(x, y + i * spacing + self.TEXT_MARGIN)
        self.text(x + self.TEXT_CENTER * self.CRATE_SPACING, y + (i+1) * spacing + self.TEXT_MARGIN, 'Beugel')
        for i in range(fles, fles+beugel):
            self.crate(x, y + i * spacing + self.TEXT_MARGIN * 2)

    def save(self, filename):
        plt.savefig(filename, orientation='portrait', format='eps')


Page(['Spoeder', 'Strucca', 'Asperge', 'Luxe']).save('out.eps')
Page(['Shiiiit', 'HO-OH', 'Goblina', 'Ilias']).save('out2.eps')
