def Add(nums: str) -> int:
    if not nums:
        return 0
    
    if ",\n" in nums or "\n," in nums or ",," in nums or nums.endswith(",") or nums.endswith("\n"):
        raise ValueError("Invalid input format")
    
    corrected_nums = nums.replace("\n", ",")
    
    try:
        number_list = [int(n) for n in corrected_nums.split(",")]
        return sum(number_list)
    except ValueError:
        raise ValueError("Invalid input format")