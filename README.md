## python-aminobots
Library for create bots in Amino

For more information join the discord server: https://discord.gg/mWJfZ2eTFc

# Scheduled Release
`01/01/2022 - 00:00 UTC+03:00`

# Documentation

# Installing (coming soon)
`pip install aminobots`

## Importable in aminobots

```python
from aminobots import (
    Amino, AsyncAmino,
    AminoBot, AsyncAminoBot,
    Context, AsyncContext,
    Command,
    amino, exceptions, types,
    aminobot,
    utils
)

from aminobots.amino import *
from aminobots.aminobot import *
from aminobots.exceptions import *
from aminobots.types import *
from aminobots.utils.apis import *
from aminobots.utils.decorators import *
```


## Amino
class to send requests synchronously to the Amino API

Path: `aminobots.amino.synchronous`

## AsyncAmino
class to send requests asynchronously to the Amino API

Path: `aminobots.amino.asynchronous`

## AminoBot
Path: `aminobots.aminobot.synchronous`

With AminoBot you can make a synchronous bot.

## AsyncAminoBot
Path: `aminobots.aminobot.asynchronous`

AsyncAminoBot is the AminoBot class but asynchronous.

## Context
class made to be used synchronously with the AminoBot class

Path: `aminobots.aminobot.synchronous`

## AsyncContext
class made to be used asynchronously with the AsyncAminoBot class

Path: `aminobots.aminobot.asynchronous`

## Command
class to manage a command

Path: `aminobots.aminobot`
