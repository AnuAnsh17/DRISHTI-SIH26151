# Evaluation Plan and Metrics
## SIH26151 — Dark web threat actor de-anonymization

### Overview
This document defines the evaluation methodology, metrics, and success criteria for the SIH26151 platform. It provides a structured approach to assessing system performance across all functional components using the synthetic dark web lab and other validation techniques.

### Evaluation Philosophy

1. **Component-Level Validation**: Each subsystem evaluated independently before integration testing
2. **Ground Truth Comparisons**: Performance measured against known relationships in synthetic lab
3. **Realistic Expectations**: Metrics reflect attainable performance for student project constraints
4. **Explainability Focus**: Evaluation includes assessment of transparency and traceability
5. **False Positive Sensitivity**: Special attention to minimizing erroneous attributions
6. **Temporal Awareness**: Evaluation includes time-based performance and concept drift handling

### Evaluation Components

#### 1. Collection Subsystem Evaluation
**Objective**: Assess effectiveness of data acquisition from various sources

**Metrics**:
- **Coverage Rate**: Percentage of target data sources successfully accessed
  - Target: ≥80% for authorized/synthetic sources
- **Data Completeness**: Score of expected fields populated per data type
  - Target: ≥90% completeness for critical fields
- **Collection Latency**: Time from data availability to system ingestion
  - Target: <1hour for near real-time sources
- **Error Rate**: Percentage of collection attempts failing due to recoverable errors
  - Target: <5% error rate
- **Source Reliability Detection**: Ability to identify and weight source quality
  - Measured through controlled source reliability injection

**Evaluation Methods**:
- Controlled source availability testing
- Synthetic data injection with known drop-out patterns
- Source reputation feeding experiments
- Timed collection intervals

#### 2. Normalization Subsystem Evaluation
**Objective**: Assess effectiveness of data standardization and validation

**Metrics**:
- **Format Conversion Accuracy**: Percentage of data correctly converted to target schema
  - Target: ≥95% accuracy
- **Duplicate Detection Rate**: Ability to identify duplicate records
  - Target: ≥90% precision, ≥80% recall
- **Validation Precision**: Correct identification of invalid/malformed data
  - Target: ≥85% precision
- **Processing Overhead**: Additional time required for normalization
  - Target: <20% increase over raw ingestion time

**Evaluation Methods**:
- Known format variations injection
- Duplicate record introduction
- Malformed data testing
- Performance benchmarking

#### 3. Extraction Subsystem Evaluation
**Objective**: Assess effectiveness of entity and relationship identification

**Metrics**:
- **Entity Mention Precision**: Percentage of extracted mentions that are correct
  - Target: ≥80% precision
- **Entity Mention Recall**: Percentage of actual mentions that are extracted
  - Target: ≥70% recall
- **Relationship Extraction F1**: Harmonic mean of precision/recall for relationships
  - Target: ≥0.70 F1-score
- **Confidence Calibration**: Alignment of confidence scores with empirical accuracy
  - Target: Brier score <0.15

**Evaluation Methods**:
- Labeled dataset extraction testing
- Confidence threshold tuning
- Entity type-specific evaluation
- Relationship pattern validation

#### 4. Resolution Subsystem Evaluation
**Objective**: Assess effectiveness of entity disambiguation and linking

**Metrics**:
- **Resolution Precision**: Percentage of resolved entity links that are correct
  - Target: ≥85% precision (critical for attribution systems)
- **Resolution Recall**: Percentage of actual entity links that are resolved
  - Target: ≥75% recall
- **False Link Rate**: Percentage of resolved links that are incorrect (must be minimized)
  - Target: <5% false link rate
- **Cluster Purity**: Homogeneity of resolved entities (all mentions refer to same real entity)
  - Target: ≥80% purity
- **Resolution Stability**: Consistency of resolutions over time with new evidence
  - Target: ≥90% stability for resolved entities

**Evaluation Methods**:
- Labeled entity resolution datasets
- Synthetic data with known ground truth entities
- Confidence threshold analysis
- Temporal consistency validation

#### 5. Correlation Subsystem Evaluation
**Objective**: Assess effectiveness of multi-evidence analysis and pattern detection

**Metrics**:
- **Infrastructure Correlation Accuracy**: Correct identification of shared infrastructure
  - Target: ≥80% precision, ≥70% recall
- **Stylometric Similarity Accuracy**: Correct identification of same-author texts
  - Target: ≥75% precision, ≥65% recall (adjusted for short text limitations)
- **Behavioral Similarity Accuracy**: Correct identification of similar behavior patterns
  - Target: ≥70% precision, ≥60% recall
- **Wallet Linkage Accuracy**: Correct identification of wallet/entity relationships
  - Target: ≥80% precision (address reuse is strong evidence)
- **Evidence Combination Effectiveness**: Improvement over individual evidence types
  - Target: ≥20% F1-score improvement over best single evidence type

**Evaluation Methods**:
- Controlled correlation scenario testing
- Evidence ablation studies
- Confidence score calibration
- False positive rate measurement

#### 6. Graph Subsystem Evaluation
**Objective**: Assess effectiveness of graph storage, querying, and analysis

**Metrics**:
- **Query Response Time**: Time to execute common graph queries
  - Target: <2s for attribution path queries (<3 hops)
- **Graph Update Latency**: Time to add new entities/relationships and make queryable
  - Target: <5s for batch updates
- **Traversal Efficiency**: Performance of neighborhood expansion queries
  - Target: <3s for 2-hop neighborhood queries
- **Storage Efficiency**: Storage space per entity/relationship
  - Target: <1KB average per node/relationship
- **Concurrent Query Handling**: Performance under multiple simultaneous queries
  - Target: <5s 95th percentile for 10 concurrent queries

**Evaluation Methods**:
- Query benchmarking suites
- Load testing with varying concurrency
- Storage utilization measurement
- Index effectiveness testing

#### 7. Scoring Subsystem Evaluation
**Objective**: Assess effectiveness of evidence combination and attribution confidence

**Metrics**:
- **Attribution Precision**: Percentage of attribution hypotheses that are correct
  - Target: ≥80% precision (high confidence threshold)
- **Attribution Recall**: Percentage of actual linkages that are identified
  - Target: ≥60% recall (acknowledging difficulty)
- **False Attribution Rate**: Percentage of incorrect linkages accepted as correct
  - Target: <3% false attribution rate (critical requirement)
- **Confidence Calibration**: Alignment of predicted probabilities with empirical accuracy
  - Target: Brier score <0.10, responsiveness to evidence
- **Explainability Score**: Ability to trace confidence to specific evidence contributions
  - Target: ≥80% of confidence traceable to specific evidence items
- **Alternative Hypothesis Generation**: Quality of competing explanations considered
  - Target: ≥70% of relevant alternatives generated

**Evaluation Methods**:
- Labeled attribution hypothesis testing
- Calibration analysis (reliability diagrams)
- Explainability auditing
- Alternative hypothesis completeness checking

#### 8. End-to-End System Evaluation
**Objective**: Assess overall system performance in realistic scenarios

**Metrics**:
- **Investigation Cycle Time**: Time to complete a typical investigation workflow
  - Target: <30 minutes for guided synthetic lab scenario
- **Analyst Satisfaction**: Subjective assessment of usefulness and usability
  - Target: ≥4/5 average rating in expert review
- **Evidence Traceability**: Ability to follow conclusions back to raw data
  - Target: ≥90% traceability for attribution conclusions
- **Scalability Indicator**: Performance with increasing data volumes
  - Target: <50% performance degradation at 2x data volume
- **Robustness Score**: Performance degradation with missing evidence types
  - Target: <30% performance loss when one evidence type unavailable

**Evaluation Methods**:
- Full scenario testing with synthetic lab
- Expert review panels
- Ablation studies (removing components)
- Performance scaling tests

### Evaluation Methodology

#### Synthetic Lab Evaluation
- **Primary Validation Mechanism**: Use of /home/erebus/data/synthetic/ with known ground truth
- **Regular Testing**: Automated evaluation runs during development
- **Scenario-Based Testing**: Specific test cases from GROUND_TRUTH.md
- **Regression Testing**: Ensure new changes don't break existing functionality

#### Hold-Out Validation
- **Data Splitting**: Split synthetic data into training/evaluation sets
- **Temporal Validation**: Train on earlier data, test on later data
- **Cross-Scenario Validation**: Train on some scenarios, test on others

#### Expert Review
- **Analyst Panel**: Involve 2-3 domain experts in periodic reviews
- **Blind Testing**: Experts evaluate system outputs without knowing expected outcomes
- **Feedback Incorporation**: Use expert feedback to refine metrics and thresholds

#### Ablation Studies
- **Component Removal**: Temporarily disable subsystems to measure impact
- **Evidence Withholding**: Remove specific evidence types to measure dependency
- **Simplification Testing**: Evaluate performance with reduced feature sets

### Success Criteria

#### Minimum Viable Product (MVP) Thresholds
To be considered SIH-ready, the system must meet these minimum thresholds:

1. **Attribution Precision**: ≥75% at ≥60% recall operating point
2. **False Attribution Rate**: ≤5%
3. **False Link Rate**: ≤10% in entity resolution
4. **Explainability**: ≥70% of confidence traceable to evidence
5. **End-to-End Functionality**: Complete workflow from collection to report
6. **Synthetic Lab Performance**: Successfully resolve ≥60% of ground truth linkages

#### Stretch Goals (for outstanding performance)
1. **Attribution Precision**: ≥85% at ≥70% recall
2. **False Attribution Rate**: ≤2%
3. **False Link Rate**: ≤5%
4. **Explainability**: ≥90% traceability
5. **Real-World Applicability**: Demonstrated utility on authorized public datasets

### Reporting and Documentation

#### Evaluation Reports
Each evaluation cycle should produce:
- **Metrics Dashboard**: Quantitative performance across all metrics
- **Failure Analysis**: Detailed examination of incorrect decisions
- **Component Health**: Individual subsystem performance
- **Recommendations**: Prioritized improvements for next iteration
- **Reproducibility Pack**: Data, configurations, and scripts to reproduce results

#### Metric Tracking
- **Baseline Establishment**: Initial measurement before optimization
- **Progress Monitoring**: Regular tracking during development
- **Regression Detection**: Alerts for significant performance degradation
- **Goal Attainment**: Clear visualization of progress toward thresholds

### Resource Requirements

#### Data Requirements
- Synthetic dark web lab data (provided in /data/synthetic/)
- Additional test scenarios as needed
- Ground truth documentation for validation

#### Computational Requirements
- Moderate processing power for batch evaluation
- Storage for multiple dataset versions
- Network connectivity for synthetic data generation (if applicable)

#### Human Requirements
- 1-2 evaluators for metric calculation and analysis
- Domain experts for expert review panels
- Development team for implementing improvements based on feedback

### Continuous Evaluation Approach

#### Development Phase
- **Unit Testing**: Continuous testing of individual components
- **Integration Testing**: Regular combined subsystem testing
- **Synthetic Lab Runs**: Automated evaluation after significant changes
- **Metrics Dashboard**: Real-time visualization of key metrics

#### Pre-Demonstration Phase
- **Comprehensive Evaluation**: Full end-to-end assessment
- **Expert Review**: Independent analysis by domain specialists
- **Stress Testing**: Performance under expected load conditions
- **Final Validation**: Confirmation of MVP threshold attainment

#### Post-Deployment Phase
- **Operational Monitoring**: Ongoing performance tracking in deployment
- **User Feedback Collection**: Analyst satisfaction and usability feedback
- **Periodic Re-Evaluation**: Scheduled comprehensive assessments
- **Adaptation Planning**: Updates based on operational experience

### Risk Mitigation for Evaluation

#### Overfitting to Synthetic Data
- **Mitigation**: Use multiple synthetic data variations
- **Hold-Out Sets**: Reserve portion of synthetic data for final validation
- **Concept Drift Testing**: Evaluate performance on temporally shifted data

#### Metric Gaming
- **Mitigation**: Use blinded evaluation where possible
- **Multiple Metric Types**: Combine precision/recall with calibration and explainability
- **Expert Oversight**: Expert review to detect metric manipulation

#### Resource Constraints
- **Mitigation**: Prioritize metrics Most critical to success
- **Efficient Automation**: Automate as much evaluation as possible
- **Focus on Indicators**: Use proxy metrics when direct measurement expensive

#### Subjectivity in Expert Review
- **Mitigation**: Use structured evaluation rubrics
- **Multiple Reviewers**: Average scores across 2-3 experts
- **Calibration Sessions**: Align reviewers on scoring criteria

### Conclusion
This evaluation plan provides a comprehensive framework for assessing the SIH26151 platform's performance. By measuring both component-level effectiveness and end-to-end system capabilities, it ensures that the platform meets its objectives of accurate, explainable, and timely threat actor attribution while minimizing false positives. The focus on the synthetic dark web lab with known ground truth enables objective validation, while the inclusion of expert review and operational considerations ensures practical utility.