import pandas
import tkinter
from tkinter import filedialog
import os
import time
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication

class Importer:
    file_name_processed_record = []

    @staticmethod
    def operation_name_to_function(operation_string_name):
        operation_dictionary = {"addition": Addition.add_number, "subtraction": Subtraction.subtract_number,
                                "multiplication": Multiplication,
                                "division": Division.divide_number}
        return operation_dictionary.get(operation_string_name)

    @staticmethod
    def calculate_data_file():
        """Prompts user for file selection to processes file(s) """
        return Importer.perform_calculation_on_data_file(Importer.file_dialog_navigator())

    @staticmethod
    def file_dialog_navigator():
        """Opens tkinter File Dialog for User to Select .csv data files"""
        data_file_list = []
        root_path = tkinter.Tk()
        root_path.title('Calculator File system Import')
        root_path.withdraw()
        data_file_list = filedialog.askopenfiles(mode='r', filetypes=[('CSV Files', '*.csv')])
        return data_file_list

    @staticmethod
    def perform_calculation_on_data_file(selected_data_files):
        """ Takes dictionary of operation and dataframe for per row calculation"""
        data_file_batch = []
        data_file_counter = 0

        print("... Preprocessing Datafile Batch! ...")

        for data_operation, data_frame_values, current_file_name in Importer.data_file_zipped(selected_data_files):
            calculator_method_call = Importer.operation_name_to_function(data_operation)

            results_column = data_frame_values.iloc[:, -1]
            data_to_be_calculated = data_frame_values.drop('result', axis=1)

            current_processing_file_name = []
            current_data_operation = []
            current_processing_time = []
            current_calculation_record_number = []
            calculator_row_results = []

            for row_index_value, row_data in data_to_be_calculated.iterrows():
                try:
                    calculator_row_results.append(
                        calculator_method_call(row_data[row_data.notna()]))  # .get_calculator_result()
                    current_processing_time.append(Importer.get_unix_time())
                    current_processing_file_name.append(current_file_name)
                    current_calculation_record_number.append(row_index_value)
                    current_data_operation.append(data_operation)

                except ArithmeticError:
                    print("oops")

            data_file_batch.append([zip(current_calculation_record_number,
                                        current_processing_file_name, current_processing_time,
                                        current_data_operation, calculator_row_results, results_column),
                                    selected_data_files, data_file_counter])
            data_file_counter += 1

            print("Currently processing: " + current_file_name + ". File: " +
                  str(data_file_counter) + " of " + str(len(selected_data_files)))

        print("\n... Commencing Validation Process ...\n")
        Importer.write_result_to_csv(data_file_batch)
        print("\n... Preparing to Write Results ...\n")
        print("Processing Complete!")

    @staticmethod
    def write_result_to_csv(file_batch):
        """Writes calculator result to result folder
        with unix time stamp, filename, record number, operation"""

        for proccesed_item, data_file_list, processing_index in file_batch:
            current_data_file = data_file_list[processing_index]
            results_data_frame = pandas.DataFrame(list(proccesed_item), columns=['calculation_record', 'file_name',
                                                                                 'timestamp', 'operation',
                                                                                 'calculated_results',
                                                                                 'expected_results'])
            csv_file_path = Importer.data_file_to_path(current_data_file)
            Importer.create_results_directory(csv_file_path)
            result_file_name = 'results_' + current_data_file.name.split("/")[-1]

            # Internal Check of Expected versus Calculated Results
            Importer.check_sum_data(results_data_frame['calculated_results'],
                                    results_data_frame['expected_results'], result_file_name)

            processed_file_name_path = os.path.join(csv_file_path, result_file_name)
            try:
                results_data_frame.to_csv(processed_file_name_path)
            except:
                print("Something went wrong")

    @staticmethod
    def check_sum_data(calculated_results, true_results, file_name):
        validate_data = pandas.DataFrame(abs(calculated_results) - abs(true_results))
        if (sum(validate_data)) == 0:
            print("Internal Verification for " + file_name + " Successful!")
        else:
            print("Error: Mismatch in Calculated and Expected Results for " + file_name + " at line(s): "
                  + str(validate_data[validate_data.iloc[0] > 0]))

    @staticmethod
    def data_file_zipped(imported_data_files):
        """Processes file operations with data frame"""
        data_file_names = Importer.data_file_path_to_name(imported_data_files)
        data_file_operations_list = Importer.file_name_to_operation(
            Importer.data_file_path_to_name(imported_data_files))
        data_file_data_frames_list = Importer.data_file_to_dataframe(imported_data_files)
        return zip(data_file_operations_list, data_file_data_frames_list, data_file_names)

    @staticmethod
    def file_name_to_operation(list_of_files):
        """Parses file.name to embedded operation"""
        data_file_operation_list = []
        for file_name in list_of_files:
            data_file_operation_list.append(file_name.split("_")[0])
        return data_file_operation_list

    @staticmethod
    def data_file_to_path(data_file):
        """Takes data file object and parses path"""
        data_file_path_root = []
        data_file_name_path = data_file.name
        file_name = data_file_name_path.split("/")[-1]
        return data_file_name_path.replace(file_name, 'results')

    @staticmethod
    def write_error_exception_log():
        """Record error and file name"""

    @staticmethod
    def create_results_directory(directory_path):
        """Utilizes data_file_path to generate results folder"""
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        return True

    @staticmethod
    def data_file_to_dataframe(data_files):
        """Takes list of data files and reads them into a list of data frames"""
        parsed_data_frames = []
        for data in data_files:
            parsed_data_frames.append(pandas.read_csv(data.name))
        return parsed_data_frames

    @staticmethod
    def data_file_path_to_name(data_files_list):
        """Takes list of file paths and returns filename(s) as list"""
        data_file_name_list = []
        for file in data_files_list:
            data_file_name_list.append(file.name.split("/")[-1])
        return data_file_name_list

    @staticmethod
    def store_processed_file_name(file_name: str):
        """Appends file_name_list with current file name"""
        Importer.file_name_processed_record.append(file_name)

    @staticmethod
    def get_last_processed_file_name():
        """Returns the last str appended to file_name_list"""
        return Importer.file_name_processed_record[-1]

    @staticmethod
    def get_unix_time():
        """Returns Unix Timestamp"""
        return int(time.time())
