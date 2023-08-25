# from unittest import TestCase
# import asyncio

# from cat import Cat

# async def herd(cat, direction):
#     cat.pet()
#     return await cat.move(direction)

# class Tests(TestCase):

#     def test_forward(self):
#         garfield = Cat('Garfield')
#         # self.assertTrue(garfield.move('forward'))

#         # self.assertTrue(herd(garfield, 'forward'))

#         result = asyncio.run(herd(garfield, 'forward'))
#         print(result)
#         self.assertTrue(result)



import pytest
import cat

async def herd(cat, direction):
    cat.pet()
    return await cat.move(direction)


# @pytest.mark.asyncio
async def test_forward():
    garfield = cat.Cat('Garfield')
    result = await herd(garfield, 'forward')
    assert result

# @pytest.mark.asyncio
async def test_backward():
    garfield = cat.Cat('Garfield')
    result = await herd(garfield, 'backward')
    assert result

# @pytest.mark.asyncio
async def test_left():
    garfield = cat.Cat('Garfield')
    result = await herd(garfield, 'left')
    assert result

# @pytest.mark.asyncio
async def test_right():
    garfield = cat.Cat('Garfield')
    result = await herd(garfield, 'right')
    assert result