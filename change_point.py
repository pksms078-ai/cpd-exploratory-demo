from typing import List, Sequence

class ChangePointDetector:
    """
    Simple mean-shift based Change Point Detector.
    Detects a single large shift in average.
    """

    def __init__(self, threshold: float = 5.0):
        self.threshold = threshold

    def detect(self, data: Sequence[float]) -> List[int]:
        if len(data) < 2:
            return []

        baseline_mean = data[0]

        for i in range(1, len(data)):
            current_mean = sum(data[:i]) / i
            if abs(current_mean - baseline_mean) >= self.threshold:
                return [i]

        return []

cat << 'EOF' > src/cpd_exploratory/change_point.py
from typing import List, Sequence

class ChangePointDetector:
    """
    Simple mean-shift based Change Point Detector.
    Detects a single large shift in average.
    """

    def __init__(self, threshold: float = 5.0):
        self.threshold = threshold

    def detect(self, data: Sequence[float]) -> List[int]:
        if len(data) < 2:
            return []

        cps = []
        prev_mean = data[0]

        for i in range(1, len(data)):
            current_mean = sum(data[:i]) / i
            if abs(current_mean - prev_mean) >= self.threshold:
                cps.append(i)
                break
            prev_mean = current_mean

        return cps
EOF
