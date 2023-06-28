import unittest, os
from sniff_data import open_data_to_dict, sniff_and_dump


class SniffDataTest(unittest.TestCase):
    path_for_input_file = "./data"
    sample_input_filenames = ["data_1.json", "data_1.json"]
    sample_output_filename = "test_output_sample.json"
    path_for_output_file = "./schema"
    
    def test_file_import_to_dict(self):
        # return value must be a dict instance, if otherwise, an error must have occured.
        for file in self.sample_input_filenames:
            return_value = open_data_to_dict(json_datafile=file, input_dir=self.path_for_input_file)
            self.assertIsInstance(return_value, dict, "Data file expected to successfully open and be mapped into Python dict")

    def test_sniff_and_file_output(self):
        sample_dict = open_data_to_dict(json_datafile=self.sample_input_filenames[0], input_dir=self.path_for_input_file)
        return_value = sniff_and_dump(sample_dict, self.sample_output_filename, output_dir=self.path_for_output_file)
        self.assertTrue(return_value, "Program failed expectation to write python obj to a file.")

    @classmethod
    def tearDown(cls):
        try:
            os.remove(f"{cls.path_for_output_file}/{cls.sample_output_filename}")
        except Exception:
            pass
    


unittest.main()
