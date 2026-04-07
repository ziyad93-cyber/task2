import math

class StatEngine:
    def init(self, data):
        if not isinstance(data, (list, tuple)):
            raise TypeError("Please provide data as a list or tuple.")

        self.data = []
        for item in data:
            if isinstance(item, (int, float)):
                self.data.append(float(item))
            else:
                raise TypeError(f"Invalid value '{item}'. Only numbers are allowed.")

        if len(self.data) == 0:
            raise ValueError("Data cannot be empty.")

    def get_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count

    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)

        if n % 2 == 1:
            return sorted_data[n // 2]

        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2

    def get_mode(self):
        counts = {}

        for num in self.data:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        max_count = max(counts.values())

        if max_count == 1:
            return "No mode (all values are unique)"

        modes = []
        for num, count in counts.items():
            if count == max_count:
                modes.append(num)

        return modes

    def get_variance(self, is_sample=True):
        n = len(self.data)
        mean = self.get_mean()

        squared_diff_sum = 0
        for x in self.data:
            squared_diff_sum += (x - mean) ** 2

        if is_sample:
            if n < 2:
                raise ValueError("Need at least 2 values for sample variance.")
            divisor = n - 1
        else:
            divisor = n

        return squared_diff_sum / divisor

    def get_standard_deviation(self, is_sample=True):
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)

    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()

        if std_dev == 0:
            return []

        outliers = []

        for x in self.data:
            z_score = abs((x - mean) / std_dev)
            if z_score > threshold:
                outliers.append(x)

        return outliers