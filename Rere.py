import os
os.environ["OPENAI_API_KEY"] = "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"

from codeinterpreterapi import CodeInterpreterSession

from codeinterpreterapi.config import settings

settings.VERBOSE = True
async def main():
    # create a session
    session = CodeInterpreterSession(model="gpt-3.5-turbo")
    await session.astart()

    # generate a response based on user input
    response = await session.generate_response(
        "Plot the bitcoin chart of 2023 YTD"
    )

    # output the response (text + image)
    print("AI: ", response.content)
    for file in response.files:
        file.show_image()

    # terminate the session
    await session.astop()


if __name__ == "__main__":
    import asyncio
    # run the async function
    asyncio.run(main())
