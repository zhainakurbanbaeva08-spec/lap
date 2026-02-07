nums=[1,2,3,4,5,6,7,8,9]
analyze_numbers=lambda nums: list(
    map(
        lambda x: x**2,
        filter(
            lambda x: (
                (x%3==0 or x%5==0) and
                (x%15!=0) and
                (len(str(abs(x)))%2==1)
            ),
            nums
        )
    )
)

print(analyze_numbers(nums))