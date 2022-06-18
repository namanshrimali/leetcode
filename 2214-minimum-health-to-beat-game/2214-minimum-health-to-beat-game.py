class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        if armor == 0:
            return sum(damage) + 1
        max_effective_armour = 0
        total_damage = 0
        for level_damage in damage:
            total_damage += level_damage
            max_effective_armour = max(max_effective_armour, min(level_damage, armor))
        return total_damage - max_effective_armour + 1
        