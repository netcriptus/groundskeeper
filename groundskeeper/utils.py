def list_to_bullet_point(elements, attr=None):
    if attr:
        elements = [getattr(element, attr) for element in elements]
    return '\n'.join(elements)


async def send_and_log(ctx, msg):
    print(msg)
    return await ctx.send(msg)
