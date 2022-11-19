import yaml, os
from yamlinclude import YamlIncludeConstructor



class Asd:
    def dddr(self,path):
        # fpath = os.path.dirname(os.path.dirname(__file__))
        # Path = lambda p: os.path.join(fpath, p)
        YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)
        # p = Path(fpath, path)
        with open(path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data


if __name__ == '__main__':
    asd =Asd()
    path = 'a.yaml'
    t = asd.dddr(path)
    print(t)
