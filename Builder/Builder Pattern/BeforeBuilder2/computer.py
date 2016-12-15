"""
Solves constructor proliferation problem. of BeforeBUilder1, but we got a new one setting directly parameters.
Solution : BeforeBuilder3.
            it uses a  mycomputer to build a features and returns a fully funtional object

            Again there is a ordering problem.. order of creation see Builder4
"""
class Computer(object):

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self.case))
        print('\t{:>10}: {}'.format('Mainboard', self.mainboard))
        print('\t{:>10}: {}'.format('CPU', self.cpu))
        print('\t{:>10}: {}'.format('Memory', self.memory))
        print('\t{:>10}: {}'.format('Hard drive', self.hard_drive))
        print('\t{:>10}: {}'.format('Video card', self.video_card))





