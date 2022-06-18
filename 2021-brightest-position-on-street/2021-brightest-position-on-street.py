class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        light_map = {}
        for position, light_range in lights:
            start, end = position - light_range, position + light_range + 1 
            light_map[start] = light_map.get(start, 0) + 1
            light_map[end] = light_map.get(end, 0) - 1
        max_brightness, brightness_idx = -float('inf'), -1
        curr_brightness = 0
        for position in sorted(light_map.keys()):
            curr_brightness += light_map[position]
            if curr_brightness > max_brightness:
                max_brightness = curr_brightness
                brightness_idx = position
        return brightness_idx