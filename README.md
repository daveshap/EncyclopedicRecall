# Encyclopedic Recall Service

Offline encyclopedia service for Raven. Provides encyclopedic knowledge about the world in real-time by automatically posting knowledge into the Nexus (stream of consciousness). 

## Basic Functionality

Operational loop

1. Update local copy of Stream of Consciousness (SOC) from Nexus
2. Filter out responses from self
3. Parse SOC for most interesting terms (filter stop words, n-grams, etc), ex. `Iranian labor law`
4. Search offline index/data for best matches
5. Post best encyclopedia entries into SOC

## Improvements

- Use indexing service such as SOLR
- Use semantic search neural network such as BERT
