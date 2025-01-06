class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0] * len(boxes)
        for cur_box in range(len(boxes)):
            if boxes[cur_box] == "1":
                for new_pos in range(len(boxes)):
                    res[new_pos] += abs(new_pos - cur_box)
        
        return res