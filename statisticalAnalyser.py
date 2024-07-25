"""
Author: Ricardo Tassio
Note: Please refer to the README.md file for detailed instructions on installation, usage, and prerequisites.
"""

class StatisticalAnalyzer:
    """
    A class designed to perform statistical analysis on a dataset composed of numerical data. This class
    provides methods to calculate various statistical metrics such as mean, variance, standard deviation,
    minimum, maximum, and median.

    Attributes:
        numerical_data (list of float): A list that stores the numerical data for analysis.
    """

    def __init__(self):
        """
        Initializes a new instance of the StatisticalAnalyzer class.
        This constructor method sets up an empty list to store numerical data, preparing the instance
        for data reading and analysis.
        """
        self.numerical_data = []

    def read_data_from_file(self, file_path: str) -> None:
        """
        Reads numerical data from a specified file and stores it in the numerical_data attribute. 
        Each line in the file should contain one floating-point number.

        Parameters:
            file_path (str): The path to the file that contains the numerical data.

        Raises:
            IOError: If the file cannot be opened or read.
        """
        try:
            with open(file_path, 'r') as file:
                self.numerical_data = [float(line.strip()) for line in file if line.strip()]
        except IOError as e:
            print(f"An error occurred while trying to read the file: {e}")

    def calculate_mean(self) -> float:
        """
        Calculates and returns the arithmetic mean of the numerical data.

        Returns:
            float: The mean of the data, or 0.0 if the data list is empty.
        """
        if not self.numerical_data:
            return 0.0
        return sum(self.numerical_data) / len(self.numerical_data)

    def calculate_variance(self) -> float:
        """
        Calculates and returns the variance of the numerical data, a measure of the dispersion of the dataset.

        Returns:
            float: The variance of the data, or 0.0 if the data list is empty.
        """
        mean = self.calculate_mean()
        return sum((x - mean) ** 2 for x in self.numerical_data) / len(self.numerical_data) if self.numerical_data else 0.0

    def calculate_standard_deviation(self) -> float:
        """
        Calculates and returns the standard deviation of the numerical data, which is the square root of the variance.
        It provides a measure of how spread out the numbers in a data set are.

        Returns:
            float: The standard deviation of the data, or 0.0 if the data list is empty.
        """
        return self.calculate_variance() ** 0.5

    def calculate_minimum(self) -> float:
        """
        Finds and returns the minimum value from the numerical data.

        Returns:
            float: The smallest number in the data, or 0.0 if the data list is empty.
        """
        return min(self.numerical_data) if self.numerical_data else 0.0

    def calculate_maximum(self) -> float:
        """
        Finds and returns the maximum value from the numerical data.

        Returns:
            float: The largest number in the data, or 0.0 if the data list is empty.
        """
        return max(self.numerical_data) if self.numerical_data else 0.0

    def calculate_median(self) -> float:
        """
        Calculates and returns the median of the numerical data, which is the middle value when the data
        list is ordered. If the number of elements is even, the median is the average of the two middle numbers.

        Returns:
            float: The median of the data, or 0.0 if the data list is empty.
        """
        num_items = len(self.numerical_data)
        if not num_items:
            return 0.0
        sorted_data = sorted(self.numerical_data)
        mid_index = num_items // 2
        if num_items % 2 == 0:
            return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
        else:
            return sorted_data[mid_index]

def main():
    """
    Main function to create an instance of StatisticalAnalyzer, read data, and print statistical results.
    """
    data_analyzer = StatisticalAnalyzer()
    data_analyzer.read_data_from_file('sample_data.txt')
    print(f"Mean: {data_analyzer.calculate_mean()}")
    print(f"Variance: {data_analyzer.calculate_variance()}")
    print(f"Standard Deviation: {data_analyzer.calculate_standard_deviation()}")
    print(f"Minimum: {data_analyzer.calculate_minimum()}")
    print(f"Maximum: {data_analyzer.calculate_maximum()}")
    print(f"Median: {data_analyzer.calculate_median()}")

if __name__ == '__main__':
    main()
