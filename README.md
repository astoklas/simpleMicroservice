# simpleMicroservice
Simple Testbed for a Application built around Microservices. The Application consists of 4 parts: 
- Collector
- Queue
- Worker
- Controller

Main goal is to get knowledge on a distributed, containerized and microservice based application.
A collector collets lines of information from a file/web and put them into a queue.
The worker analysis the data and split it into words, building a statistical view on how many and which words have been used.
Flexible scaline by adding collectors or workers.

A clear nonsense project with an educationonal touch ;)

##Collector

## Queue
A redis based DB used to asyncronously queue the Strings collected by the collector and used by the works.
Also contains the statistical part of the worker output.

## Worker

## Controller
