from JsonPlaceholder import JsonPlaceholder
from typing import Awaitable, cast, Generator
from asyncio import get_event_loop


blocking = JsonPlaceholder()

model, post = blocking.create_post(
    post_id=1,
    title="Welcome",
    body="Created with obrequests",
    user_id=1
)

print(model.title)

post.update(
    new_post_id=2,
    title="Not welcome",
    body="Woooo",
    user_id=2
)

post.delete()


for post in cast(Generator, blocking.posts()):
    print(post.title)


async def main() -> None:
    awaiting = JsonPlaceholder(awaiting=True)

    model, post = await cast(Awaitable, awaiting.create_post(
        post_id=1,
        title="Welcome",
        body="Created with obrequests",
        user_id=1
    ))

    print(model.title)

    await post.update(
        new_post_id=2,
        title="Not welcome",
        body="Woooo",
        user_id=2
    )

    await post.delete()

    for post in (await awaiting.posts()):  # type: ignore
        print(post.title)

    await awaiting.close()


loop = get_event_loop()
loop.run_until_complete(main())
