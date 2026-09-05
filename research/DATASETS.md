# Datasets Survey
## SIH26151 — Dark web threat actor de-anonymization

### Public and Authorized Datasets for Dark Web Research

#### Tor Project Metrics
- **SOURCE**: https://metrics.torproject.org/
- **CLAIM**: Public metrics about Tor network usage, relay statistics, and hidden service data
- **EVIDENCE**: 
  - Official Tor Project metrics portal
  - Provides historical data on relay bandwidth, user estimates, and hidden service descriptors
  - Updated regularly with anonymized, aggregate data
- **RELEVANCE**: Understanding Tor network characteristics for infrastructure analysis (#2)
- **IMPLEMENTATION IMPLEMENTATION**: Use for baseline network statistics; not for identifying specific services due to aggregation

#### GitHub - Awesome Onion Services
- **SOURCE**: https://github.com/rkit/awesome-onion-services
- **CLAIM**: Curated list of resources, tools, and datasets related to Tor hidden services
- **EVIDENCE**: 
  - Community-maintained repository
  - Links to research papers, tools, and dataset collections
  - Includes references to academic studies with published datasets
- **RELEVANCE**: Discovery of available research datasets
- **IMPLEMENTATION IMPLEMENTATION**: Reference for locating additional datasets and tools

#### Scholarly Dataset Repositories
- **SOURCE**: Various academic sources
- **CLAIM**: Research datasets published alongside academic papers on dark web analysis
- **EVIDENCE**: 
  - Examples: UCI Machine Learning Repository, Kaggle, academic paper supplementary materials
  - Studies often publish crawled marketplace data, forum posts, or transaction traces
  - Must verify authorization and ethical sourcing
- **RELEVANCE**: Potential sources for training/evaluation data
- **IMPLEMENTATION IMPLEMENTATION**: Careful review of data usage policies and ethics board approvals required

### Synthetic Data Generation Approaches

#### Markov Chain Text Generation
- **SOURCE**: https://en.wikipedia.org/wiki/Markov_chain
- **CLAIM**: Statistical model for generating text that mimics training data patterns
- **EVIDENCE**: 
  - Used in stylometry research to create controlled writing style variations
  - Can generate realistic forum/marketplace posts with specific author characteristics
  - Computationally efficient and easy to implement
- **RELEVANCE**: Generating synthetic dark web posts for stylometry evaluation (#4)
- **IMPLEMENTATION IMPLEMENTATION**: Train on legitimate text corpora; generate posts with controllable style features

#### Network Graph Generators
- **SOURCE**: https://networkx.org/documentation/stable/reference/generators.html
- **CLAIM": Algorithms for generating synthetic social and infrastructure networks
- **EVIDENCE**: 
  - Examples: Erdős–Rényi, Barabási–Albert, Watts–Strogatz models
  - Can create realistic vendor-buyer networks, service infrastructure topologies
  - Parameters control clustering, degree distribution, and community structure
- **RELEVANCE**: Creating synthetic entity relationship graphs for evaluation (#3, #5)
- **IMPLEMENTATION IMPLEMENTATION**: Use NetworkX or similar to generate ground truth graphs

#### Cryptocurrency Transaction Simulators
- **SOURCE**: https://github.com/bitcoin/bitcoin/blob/master/src/test/
- **CLAIM": Tools for generating synthetic blockchain transactions for testing
- **EVIDENCE**: 
  - Bitcoin Core includes transaction generation utilities for regtest mode
  - Libraries like bitcoinj and libbitcoin provide transaction creation APIs
  - Can simulate address reuse, mixing behaviors, and temporal patterns
- **RELEVANCE**: Generating synthetic cryptocurrency data for wallet analysis (#3)
- **IMPLEMENTATION IMPLEMENTATION**: Use regtest mode or transaction generation libraries for controlled crypto data

### Evaluation and Benchmark Datasets

#### Author Identification Datasets
- **SOURCE**: https://www.clef-initiative.eu/
- **CLAIM": Standardized datasets for authorship attribution evaluation
- **EVIDENCE": 
  - PAN (Plagiarism Analysis, Authorship Identification, and Near-Duplicate Detection) labs
  - Provides corpora with known authorship ground truth
  - Includes cross-domain, cross-topic, and style variation scenarios
- **RELEVANCE": Benchmarking stylometry approaches (#4)
- **IMPLEMENTATION IMPLEMENTATION": Adapt PAN methodology for dark web text evaluation

#### Record Linkage Datasets
- **SOURCE": https://www.cs.utexas.edu/~ml/riddle/
- **CLAIM": Benchmark datasets for record linkage and entity resolution evaluation
- **EVIDENCE": 
  - Riddle: The Record Linkage and Privacy-Preserving Techniques Dataset
  - Includes synthetic personal data with known matching relationships
  - Varies in size, complexity, and noise levels
- **RELEVANCE": Evaluating entity resolution approaches (#3)
- **IMPLEMENTATION IMPLEMENTATION": Use as reference for designing synthetic CTI entity resolution benchmarks

### Data Collection Considerations

#### Authorized Sources Only
- **PRINCIPLE": All data collection must be from publicly available, authorized, or synthetic sources
- **JUSTIFICATION": Ethical and legal compliance requirement for SIH project
- **IMPLEMENTATION": 
  - Focus on surface web discussions about dark web activities
  - Use Tor Project's public metrics and consensus data
  - Leverage academic publications with published datasets
  - Generate synthetic data for controlled evaluation

#### Data Provenance and Licensing
- **REQUIREMENT": Track source, collection method, and usage rights for all data
- **IMPLEMENTATION": 
  - Maintain provenance metadata with each dataset
  - Document any transformations or anonymization applied
  - Ensure compliance with data usage licenses and attribution requirements

#### Privacy and Anonymization
- **CONSIDERATION": Even public dark web data may contain sensitive information
- **MITIGATION": 
  - Remove or hash personally identifiable information (PII)
  - Aggregate data where possible to prevent re-identification
  - Follow data minimization principles
  - Consult with ethics board for any human subjects data

### Recommended Approach for SIH26151

1. **Phase 1: Synthetic Data Foundation**
   - Create fully controlled synthetic dark web ecosystem
   - Define ground truth relationships and attributes
   - Use for initial development and testing

2. **Phase 2: Authorized Public Data Integration**
   - Integrate Tor Project metrics and public threat intelligence feeds
   - Incorporate academic datasets with proper authorization
   - Maintain clear separation between synthetic and real data

3. **Phase 2+: Controlled Expansion**
   - Consider partnerships for authorized, limited-access research data
   - Always maintain ethical boundaries and legal compliance
   - Never engage in unauthorized access or data scraping of prohibited sources

This approach ensures scientific validity while maintaining ethical and legal compliance appropriate for a student research project.