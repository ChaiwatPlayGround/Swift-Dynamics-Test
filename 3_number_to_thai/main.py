"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        
        if number == 0:
            return "ศูนย์"

        thai_num_text = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
        thai_place_text = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน", "ล้าน"]
        
        num_str = str(number)[::-1]  # กลับลำดับตัวเลขเพื่อเริ่มจากหลักหน่วย
        result = []
        for i, digit in enumerate(num_str):
            digit = int(digit)
            if i == 0 and digit == 1 and len(num_str) > 1:  # หลักหน่วยที่ต้องอ่านว่า "เอ็ด"
                result.append("เอ็ด")
            elif i == 1 and digit == 1:  # หลักสิบที่ต้องอ่านว่า "สิบ"
                result.append("สิบ")
            elif i == 1 and digit == 2:  # หลักสิบที่ต้องอ่านว่า "ยี่สิบ"
                result.append("ยี่สิบ")
            elif digit != 0:
                result.append(thai_num_text[digit] + thai_place_text[i])
        
        return ''.join(result[::-1])  # กลับลำดับอีกครั้งเพื่อให้เป็นข้อความคำอ่าน

# ตัวอย่างการใช้งาน
solution = Solution()
print(solution.number_to_thai(1111))  # หนึ่งร้อยเอ็ด
print(solution.number_to_thai(-1))   # number can not less than 0
