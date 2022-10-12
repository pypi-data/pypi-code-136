

async def binary_history_check(min_block, max_block, check):
    max_succeeded_block = max_block
    min_failed_block = min_block
    current_block = max_succeeded_block

    max_steps = 100
    while max_steps > 0:
        max_steps -= 1
        success = await check(current_block)

        if success:
            max_succeeded_block = current_block
        else:
            min_failed_block = current_block

        if max_succeeded_block - min_failed_block == 1:
            return max_succeeded_block

        current_block = min_failed_block + (max_succeeded_block - min_failed_block) // 2

    raise Exception("Failed to find block")