import time
from collections import deque
bake = deque()


class cake():
    """O(n)"""

    def __init__(self):
        pass

    def addLayer(self, layer):
        """O(1)"""
        bake.append(layer)

    def eatLayer(self):
        """O(1)"""
        bake.popleft()

    def checkCake(self):
        """O(1)"""
        print(bake)


timer = time.time()

cakify = cake()
cakify.addLayer("chocolate")
cakify.checkCake()
cakify.addLayer('strawberry')
cakify.checkCake()
cakify.addLayer('cream')
cakify.eatLayer()
cakify.checkCake()
cakify.eatLayer()
cakify.checkCake()

print(
    f'Aprox {time.time() - timer} moments have elapsed within excecuting this segment.')
