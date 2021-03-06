import numpy as np

class fakeProfile:
    '''
    generate a fake simplified profile in order to test 
    implementations of qc-tests.
    '''

    def __init__(self, temperatures, depths, latitude=None, longitude=None, date=[1999, 12, 31, 0]):
        self.temperatures = temperatures
        self.depths = depths

        self.primary_header = {}
        self.primary_header['Number of levels'] = len(depths)
        self.primary_header['Latitude'] = latitude
        self.primary_header['Longitude'] = longitude
        self.primary_header['Year'] = date[0]
        self.primary_header['Month'] = date[1]
        self.primary_header['Day'] = date[2]
        
    def latitude(self):
        """ Returns the latitude of the profile. """
        assert self.primary_header['Latitude'] is not None, 'Latitude has not been set'
        return self.primary_header['Latitude']

    def longitude(self):
        """ Returns the longitude of the profile. """
        assert self.primary_header['Longitude'] is not None, 'Longitude has not been set'
        return self.primary_header['Longitude']

    def t(self):
        """ Returns a numpy masked array of temperatures. """
        return self.var_data(self.temperatures)

    def z(self):
        """ Returns a numpy masked array of depths. """
        return self.var_data(self.depths)

    def n_levels(self):
        """ Returns the number of levels in the profile. """
        return self.primary_header['Number of levels']

    def year(self):
        """ Returns the year. """
        return self.primary_header['Year']

    def month(self):
        """ Returns the month. """
        return self.primary_header['Month']

    def day(self):
        """ Returns the day. """
        return self.primary_header['Day']

    def var_data(self, dat):
        """ Returns the data values for a variable given the variable index. """
        data = np.ma.array(np.zeros(len(dat)), mask=True)

        for i in range(len(dat)):
            if dat[i] is not None:
                data[i] = dat[i]
        return data

