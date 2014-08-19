from copy import deepcopy

class NBC():
    def __init__(self,sample,attributes,target,smooth=0):
        self.n = len(sample)
        self.smooth = smooth
        self.attributes = attributes
        self.target = target
        self.values = {}
        for attribute in attributes:
            self.attvalues = {}
            for option in set(sample[attribute]):
                self.attvalues[option] = self.smooth
            self.values[attribute] = self.attvalues
        self.classes = {}
        for label in set(sample[target]):
            self.classes[label] = {}
            for attribute in attributes:
                subsample = sample[sample[target]==label]
                self.classes[label][attribute]=\
                    [sample[attribute][i] for i in subsample[attribute].index]
        self.ys = findys(self,sample,attributes,target)
        self.thetas = {}
        for label in set(sample[target]):
            self.thetas[label] = deepcopy(self.values)
        
        self.findthetas(sample,attributes,target)
     
    def classifier(self,sample,attributes,target):
        pass

    def findys(self,sample,attributes,target):
        self.ys = {}
        total = float(len(sample))
        for label in set(sample[target]):
            self.ys[label] = len(sample[sample[target]==label])/total
        return self.ys

    def findthetas(self,sample,attributes,target):
        #self.thetas = {}
        for keylabel in self.classes.keys():
            #self.thetas[keylabel] = {}
            for attribute in self.attributes:
                #self.thetas[keylabel][attribute] = {}
                #norm = float(len(self.classes[keylabel][attribute]))
                for point in self.classes[keylabel][attribute]:
                    self.thetas[keylabel][attribute][point] = \
                            self.thetas[keylabel][attribute].get(point,0) + 1
                norm = float(sum(self.thetas[keylabel][attribute].values()))
                for key in self.thetas[keylabel][attribute].keys():
                    self.thetas[keylabel][attribute][key] /= norm

    def __len__(self):
        return self.n
