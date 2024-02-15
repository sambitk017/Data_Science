import configparser
import pandas as pd
import os


class MTSCfg:
    def __init__(self, cfg_file_name):
        self.cfg_file_name = cfg_file_name
        self.config = configparser.RawConfigParser()
        self.config.read(self.cfg_file_name, encoding='utf-8-sig')
        self.all_mo = self.config.sections()

    def print_all_sec(self):
        mo_data = pd.Series(self.all_mo)
        print(mo_data)

    def check_cfg_order(self, sec_f, sec_s):
        # if sim udex = 1, sim exporter = 2
        sec_f_idx = self.all_mo.index(sec_f)
        sec_s_idx = self.all_mo.index(sec_s)
        if sec_f_idx > sec_s_idx:
            self.reorder_sections(sec_f_idx,sec_s_idx)
            # print("The order of MO is not proper")
        else:
            print(f"{sec_f} and {sec_s} are in right order")

    def reorder_sections(self,sec_f_idx,sec_s_idx):
        new_config = configparser.RawConfigParser()
        temp = self.all_mo[sec_f_idx]
        self.all_mo[sec_f_idx] = self.all_mo[sec_s_idx]
        self.all_mo[sec_s_idx] = temp
        added_sections = set()
        for sec in self.all_mo:
            # Check if the section has been added before
            if sec not in added_sections:
                self.add_sec_with_properties('target.cfg', sec)
                added_sections.add(sec)
        print("MO are reordered successfully ")

    def add_sec_with_properties(self,target_file,section_name):
        input_cfg = self.config
        target_config = configparser.RawConfigParser()
        if not os.path.exists(target_file):
            target_config.add_section(section_name)
            for key, value in input_cfg[section_name].items():
                target_config[section_name][key] = value
            with open(target_file, 'w') as target_file:
                target_config.write(target_file)
        else:
            if target_config.has_section(section_name):
                # Section already exists, you can choose to update or skip
                pass
            else:
                target_config.add_section(section_name)
                for key, value in input_cfg[section_name].items():
                    target_config[section_name][key] = value
                with open(target_file, 'a') as target_file:
                    target_config.write(target_file)

    def delete_section(self, section_remove_lst):
        flag = 0
        for sec in section_remove_lst:
          if sec in self.all_mo:
            self.config.remove_section(sec)
            with open(self.cfg_file_name, 'w') as config_file:
                self.config.write(config_file)
            print(f"{sec} is removed and replaced the same in the cfg file successfully")
          else:
              print(f"{sec} is does not exist in the sourcr cfg file")


cfg_name = 'MTS_FUNCTIONAL_TEST.cfg'
cfgObj = MTSCfg(cfg_name)

cfgObj.print_all_sec()

cfgObj.check_cfg_order('SIM UDEX', 'SIM Exporter')

MO_lst_to_remove = input("what MO you want to remove").split()
cfgObj.delete_section(MO_lst_to_remove)
