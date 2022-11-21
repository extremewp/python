import yaml

from common.util.yaml_util import YamlUtil


class TestReadYamlFileContent:

    def test_read_yaml_file_content(self):
        self.yml = YamlUtil()
        with open("../../testcase/config_yaml_url.yaml") as f:
            yaml_content = dict(yaml.safe_load(f)).values()
            for yaml_content in yaml_content:
                yaml_rul_name = yaml_content['yaml_basic_url']
                method_file_name = yaml_content['relation_data_url']
                if yaml_content["relation_data_url"] is None:
                    yaml_date = self.yml.read_testcase_yaml(yaml_rul_name=yaml_rul_name)

                else:
                    yaml_date = self.yml.read_testcase_yaml(yaml_rul_name=yaml_rul_name,
                                                            method_file_name=method_file_name)
                return yaml_date

