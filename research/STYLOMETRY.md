# Stylometry and Authorship Attribution
## SIH26151 — Dark web threat actor de-anonymization

### Foundations of Stylometric Analysis

#### What is Stylometry?
- **DEFINITION": Quantitative analysis of literary style using statistical and computational methods
- **CORE IDEA": Individual writing habits are largely unconscious and difficult to disguise completely
- **APPLICATION DOMAINS": 
  - Literary attribution (e.g., Shakespeare authorship debate)
  - Forensic linguistics (ransom notes, threatening letters, etc.)
  - Security analysis (malware authorship, threat actor identification)
  - Academic integrity (plagiarism detection, contract cheating)
  - Intelligence analysis (attributing anonymous communications)
- **LIMITATIONS": 
  - Not infallible; skilled mimics can evade detection
  - Style can change intentionally or due to circumstances
  - Short texts provide limited signal
  - Domain and topic can influence style independently of author
  - Requires sufficient comparative samples for reliable analysis
- **ETHICAL CONSIDERATIONS": 
  - Probabilistic nature means false positives possible
  - Should not be sole basis for accusations or legal action
  - Requires proper validation and uncertainty quantification
  - Must be combined with other evidence for strong attribution

#### Theoretical Basis
- **UNCONSCIOUS HABITS": 
  - Writers develop consistent patterns in word choice, punctuation, syntax
  - These habits are difficult to consciously control or change completely
  - Similar to biometric traits like gait or typing patterns
  - Manifest across different genres and topics to some degree
- **INDIVIDUALITY IN LANGUAGE": 
  - No two individuals use language exactly identically
  - Vocabulary preferences, syntactic tendencies, and rhetorical styles vary
  - Even in constrained formats, individual differences persist
  - Effect size varies by individual and writing context
- **STABILITY OVER TIME": 
  - Core stylistic traits show reasonable stability over months/years
  - Major shifts usually require conscious effort or significant life events
  - Gradual drift occurs naturally with experience and aging
  - Style can return to baseline after temporary deviations

### Feature Extraction Methodologies

#### Character-Level Features
- **APPROACH": Analyze patterns at the character level (including spaces and punctuation)
- **FEATURE TYPES": 
  - Character n-grams: sequences of n consecutive characters (n=2-5 typical)
  - Character frequency: relative frequency of each character (a-z, A-Z, 0-9, punctuation, space)
  - Special character usage: rates of specific punctuation, symbols, formatting
  - Whitespace patterns: space frequency, multiple spaces, tabs, line breaking habits
  - Case patterns: uppercase/lowercase ratios, capitalization habits
- **EXTRACTION TECHNIQUES": 
  - Sliding window over text to collect n-gram frequencies
  - Count vectorization with appropriate n-gram ranges
  - Normalization to relative frequencies (probabilities)
  - Feature hashing for high-dimensional sparse representations
  - Selection of most discriminative n-grams via chi-square or mutual information
- **ADVANTAGES": 
  - Language-independent (works across alphabets and languages)
  - Effective for short texts where word-level features sparse
  - Captures typing habits and keyboard patterns
  - Robust to topical variations (less semantic dependency)
  - Computationally efficient to extract and compare
- **DISADVANTAGES": 
  - Can be obfuscated through deliberate variation
  - May capture encoding or transmission artifacts rather than style
  - Less effective for very long texts where higher-level patterns dominate
  - Feature space can be very large requiring dimensionality reduction

#### Word-Level Features
- **APPROACH": Analyze patterns at the word level (tokenized text)
- **FEATURE TYPES": 
  - Word frequency: relative frequency of each word (after normalization)
  - Word n-grams: sequences of n consecutive words (n=2-4 typical)
  - Function word usage: pronouns, prepositions, articles, conjunctions
  - Content word usage: nouns, verbs, adjectives, adverbs by category
  - Vocabulary richness: type-token ratio, hapax legomena, Simpson's diversity
  - Word length distribution: average, variance, distribution shape
- **EXTRACTION TECHNIQUES": 
  - Tokenization: splitting text into words (respecting language-specific rules)
  - Normalization: lowercasing, stemming, lemmatization (language-dependent)
  - Stop word removal: optional removal of very common words
  - Vectorization: count, TF-IDF, or binary presence/absence
  - N-gram extraction: sliding window over token sequence
  - Vocabulary pruning: remove rare or extremely common words
- **ADVANTAGES": 
  - Captures vocabulary preferences and topical tendencies
  - Function words show high stability across topics
  - Content words reveal interests and expertise areas
  - Well-established in information retrieval and text mining
  - Easy to interpret and explain to human analysts
- **DISADVANTAGES": 
  - Highly dependent on topic and genre
  - Requires language-specific tokenization and normalization
  - Vocabulary sparsity creates high-dimensional sparse features
  - Vulnerable to deliberate vocabulary variation or substitution
  - Less effective for very short texts

#### Syntactic and Structural Features
- **APPROACH": Analyze grammatical structure and text organization
- **FEATURE TYPES": 
  - Sentence length: mean, variance, distribution of sentence lengths
  - Sentence complexity: clause depth, phrase structure, embedding levels
  - Part-of-speech patterns: frequency and sequences of POS tags
  - Punctuation usage: frequency, patterns, and positions of punctuation marks
  - Paragraph structure: length, organization, transition patterns
  - Text organization: discourse markers, rhetorical structure, formatting
- **EXTRACTION TECHNIQUES": 
  - Part-of-speech tagging: spaCy, Stanza, NLTK, or Stanford NLP
  - Syntactic parsing: constituency or dependency parsing (computationally expensive)
  - Sentence boundary detection: rule-based or machine learning approaches
  - Punctuation analysis: simple counting or contextual pattern matching
  - Structural analysis: heuristics for paragraphs, lists, code blocks, etc.
  - Readability metrics: Flesch-Kincaid, Gunning Fog, SMOG, etc.
- **ADVANTAGES": 
  - Captures grammatical habits less susceptible to conscious control
  - Reveals education level, language proficiency, and writing background
  - Less topic-dependent than pure word frequency features
  - Combines well with other feature types for robustness
  - Some aspects (like average sentence length) show good stability
- **DISADVANTAGES": 
  - Computationally expensive (especially parsing)
  - Requires language-specific models and resources
  - Error propagation from imperfect tagging/parsing
  - Some syntactic features show less stability than expected
  - Language resources may not exist for all languages/dialects

#### Semantic and Content Features
- **APPROACH": Analyze meaning content and thematic preferences
- **FEATURE TYPES": 
  - Topic modeling: LDA, NMF, or probabilistic latent semantic analysis
  - Semantic field preferences: distribution across word categories (emotions, actions, etc.)
  - Lexical semantics: word similarity, clustering, or embedding-based features
  - Named entity recognition: frequency and types of named entities
  - Sentiment and affect: emotional tone, polarity, and intensity patterns
  - Readability and complexity: years of education required to understand
- **EXTRACTION TECHNIQUES": 
  - Topic models: uncover latent themes in document collections
  - Word embeddings: Word2Vec, GloVe, fastText, or contextual embeddings
  - Semantic role labeling: understand predicate-argument structure
  - Sentiment analysis: lexicon-based or machine learning approaches
  - Entity recognition: spaCy, Stanza, or custom NER for domain-specific entities
  - Concept extraction: linking to knowledge bases (Wikipedia, WordNet, etc.)
- **ADVANTAGES": 
  - Captures topical interests and expertise areas
  - Reveals cognitive patterns and conceptual frameworks
  - Can distinguish authors with similar surface style but different knowledge
  - Useful for detecting topic-driven style variations
  - Connects to broader linguistic and cognitive theories
- **DISADVANTAGES": 
  - Highly topic-dependent; may not generalize across subjects
  - Requires large corpora for reliable topic modeling
  - Semantic drift can occur independently of authorial style
  - Computationally more expensive than surface feature extraction
  - Risk of capturing transient interests rather than stable traits

#### Application-Specific Features
- **APPROACH": Extract features relevant to dark web communication contexts
- **FEATURE TYPES": 
  - Platform-specific conventions: markup usage, emoji preferences, formatting
  - Community jargon: slang, acronyms, and technical terminology patterns
  - Anonymization techniques: use of pseudonyms, encryption references, OPSEC measures
  - Transaction patterns: references to payments, shipping, or fulfillment
  - Interaction patterns: reply habits, conversation initiation, dispute handling
  - Temporal patterns: posting timing, response latency, burstiness
- **EXTRACTION TECHNIQUES": 
  - Regular expressions for platform-specific patterns (BBCode, Markdown, etc.)
  - Dictionary matching for known jargon and terminology
  - Specialized parsers for transaction references (crypto addresses, amounts)
  - Temporal analysis of timestamps (timezone conversion, activity cycles)
  - Network analysis of reply graphs and interaction patterns
  - Custom feature detectors for dark web communication norms
- **ADVANTAGES": 
  - Tailored to the specific communication context
  - Captures community participation and operational patterns
  - Can reveal operational security awareness and practices
  - Complements general stylometry with domain-specific signals
  - Helps distinguish similar styles from different communities
- **DISADVANTAGES": 
  - Requires domain expertise to define relevant features
  - May not transfer well to other contexts or platforms
  - Vulnerable to changes in platform norms or community practices
  - Can be deliberately manipulated or concealed
  - Overfitting risk if features too specific to training data

### Similarity Measurement and Classification

#### Distance and Similarity Metrics
- **APPROACH": Measure similarity between texts or authors based on feature vectors
- **METRIC TYPES": 
  - Cosine Similarity: dot product of normalized vectors (0-1 scale, 1=identical)
  - Euclidean Distance: straight-line distance in feature space (lower=more similar)
  - Manhattan Distance: sum of absolute differences across dimensions
  - Mahalanobis Distance: distance accounting for feature correlations
  - Jensen-Shannon Divergence: similarity between probability distributions
  - Hamming Distance: for binary or categorical feature comparisons
  - Bhattacharyya Distance: measures overlap between statistical distributions
- **SELECTION CONSIDERATIONS": 
  - Feature space characteristics (sparse, dense, correlated, normalized)
  - Computational efficiency requirements
  - Interpretability for investigator understanding
  - Sensitivity to different types of variations
  - Robustness to noise and irrelevant features
- **NORMALIZATION REQUIREMENTS": 
  - Essential for meaningful distance comparisons
  - Z-score normalization (mean=0, std=1) for Gaussian-like features
  - Min-max scaling (min=0, max=1) for bounded features
  - Unit vector normalization for cosine similarity
  - Feature-specific normalization based on distribution characteristics
  - Avoid normalization that destroys meaningful zero values

#### Classification Approaches
- **APPROACH": Assign texts to known authors or determine if same author
- **CLASSIFICATION TYPES": 
  - Closed-set: assign to one of known authors (requires exhaustive author list)
  - Open-set: determine if text matches any known author or is unknown
  - Verification: decide if two texts are by same author (binary decision)
  - Clustering: group texts by similarity without predefined labels
  - Ranking: order candidate authors by likelihood of authorship
- **ALGORITHM TYPES": 
  - Linear Models: Logistic Regression, Linear SVM (interpretable, fast)
  - Probabilistic Models: Naive Bayes, Bayesian Networks (uncertainty quantification)
  - Tree-Based: Decision Trees, Random Forests, XGBoost (handle non-linearities)
  - Neural Networks: MLPs, CNNs, RNNs (capture complex patterns)
  - Instance-Based: K-Nearest Neighbors, Kernel Methods (local similarity)
  - Ensemble Methods: Voting, Stacking, Boosting (combine multiple approaches)
- **TRAINING CONSIDERATIONS": 
  - Sufficient samples per author for reliable modeling
  - Balance between authors to prevent bias
  - Temporal separation to prevent overfitting to time-specific artifacts
  - Topic diversity to ensure style rather than topic is learned
  - Hold-out validation to prevent overfitting and estimate generalization
- **UNCERTAINTY QUANTIFICATION": 
  - Probability outputs from probabilistic models
  - Distance thresholds with false positive/negative rates
  - Ensemble variance as proxy for prediction uncertainty
  - Calibration techniques (Platt scaling, isotonic regression)
  - Rejection option for low-confidence predictions

### Validation and Evaluation Methodologies

#### Corpus Design for Evaluation
- **ESSENTIAL CHARACTERISTICS": 
  - Known authorship ground truth (verified through independent means)
  - Sufficient samples per author for training and testing
  - Temporal separation to test stability over time
  - Topic variation to test independence from subject matter
  - Genre variation to test robustness across formats
  - Language variation if multilingual analysis is needed
  - Text length variation to test effectiveness on short vs long texts
  - Include examples of deliberate obfuscation or mimicry if relevant
- **SOURCES OF VALIDATION CORPORA": 
  - Literary works with established authorship
  - Forensic linguistics cases with judicial outcomes
  - Academic writing with verified authorship
  - Online forums with verified user identities (research ethics approved)
  - Technical documentation and code with known authors
  - Synthetic corpora with controlled style injection
  - Translation pairs (original vs translated to test robustness)
- **SPLITTING STRATEGIES": 
  - Random split: simple but may leak temporal/topic correlations
  - Stratified split: maintain author distribution across splits
  - Temporal split: train on past, test on future (tests concept drift)
  - Topic split: train on some topics, test on others (tests topic independence)
  - Author hold-out: leave one author out for testing (tests generalization)
  - Cross-validation: multiple splits for robust estimation (k-fold, leave-one-out)
- **SAMPLE SIZE REQUIREMENTS": 
  - Minimum: 5-10 texts per author for very rough estimates
  - Reliable: 20-50 texts per author for reasonable confidence
  - Robust: 50+ texts per author for high confidence results
  - Depends on text length, style stability, and feature effectiveness
  - Power analysis recommended for specific effect sizes and alpha levels

#### Evaluation Metrics
- **ACCURACY METRICS": 
  - Accuracy: proportion of correct classifications
  - Precision: true positives / (true positives + false positives)
  - Recall: true positives / (true positives + false negatives)
  - F1-Score: harmonic mean of precision and recall
  - Specificity: true negatives / (true negatives + false positives)
  - Sensitivity: same as recall (true positive rate)
- **RANKING METRICS": 
  - Mean Reciprocal Rank (MRR): average of reciprocal ranks
  - Mean Average Precision (MAP): average precision at each relevant item
  - Normalized Discounted Cumulative Gain (NDCG): weighted ranking quality
  - Precision@k: proportion of top k results that are relevant
  - Recall@k: proportion of relevant items in top k results
- **PROBABILITY METRICS": 
  - Brier Score: mean squared error of probability predictions
  - Log Loss: negative log likelihood of predicted probabilities
  - Calibration: how well predicted probabilities match empirical frequencies
  - ROC AUC: area under receiver operating characteristic curve
  - Precision-Recall Curve: especially important for imbalanced classes
- **UNCERTAINTY METRICS": 
  - Confidence Interval Width: range of plausible values for estimates
  - Prediction Interval Width: range for future observations
  - Ensemble Standard Deviation: variability across model predictions
  - Credible Interval: Bayesian analogue of confidence interval
  - Rejection Rate: proportion of cases where system abstains from decision
- **BIAS AND FAIRNESS METRICS": 
  - Disparate Impact: difference in error rates across groups
  - Equal Opportunity Difference: difference in true positive rates
  - Treatment Equality: ratio of false false positives to false negatives
  - Statistical Parity Difference: difference in positive prediction rates
  - Conservation: whether system predicts same proportion of positives as base rate

#### Validation Methodologies
- **HOLD-OUT VALIDATION": 
  - Partition data into training and testing sets
  - Train model on training set, evaluate on test set
  - Provides unbiased estimate of generalization performance
  - Requires sufficient data for meaningful split
  - Can be repeated with different random splits for robustness
- **K-FOLD CROSS-VALIDATION": 
  - Partition data into k equal parts (folds)
  - Train on k-1 folds, test on remaining fold; repeat k times
  - Average performance across folds for final estimate
  - Reduces variance compared to single hold-out split
  - Computationally more expensive but more reliable
  - Stratified k-fold maintains class distribution in each fold
- **LEAVE-ONE-OUT CROSS-VALIDATION (LOOCV)": 
  - Special case of k-fold where k = number of samples
  - Train on all but one sample, test on that sample
  - Nearly unbiased but high variance
  - Computationally expensive for large datasets
  - Useful for small datasets where every sample matters
- **TEMPORAL VALIDATION": 
  - Train on earlier texts, test on later texts from same authors
  - Tests robustness to concept drift and style evolution
  - Important for longitudinal analysis applications
  - Requires timestamped data with sufficient temporal spread
  - Can combine with other splitting strategies (temporal hold-out)
- **TOPICAL VALIDATION": 
  - Train on texts about some subjects, test on different subjects
  - Tests independence of style from topic choice
  - Critical for ensuring analysis captures author not subject
  - Requires documents with known topics or topic modeling
  - Can reveal confounds between style and topical preferences
- **ADVERSARIAL VALIDATION": 
  - Test with known obfuscation techniques and mimicry attempts
  - Measures robustness against active evasion
  - Essential for security and forensic applications
  - Requires red team or adversarial testing capability
  - Should include both skilled and naive obfuscation attempts

#### Dark Web Specific Validation Considerations
- **TEXT LENGTH CHALLENGES": 
  - Dark web posts often very short (forum replies, market listings)
  - Need to validate effectiveness on short texts (10-100 characters)
  - Character n-grams may be more effective than word-level for short texts
  - Consider minimum viable text length for reliable attribution
  - Evaluate combining multiple short texts from same author
- **TOPIC CONSTRAINTS": 
  - Dark web communities often discuss similar topics (drugs, hacking, fraud)
  - Topic independence becomes crucial to avoid false positives
  - Validate on texts discussing same topic by different authors
  - Validate on different topics by same author
  - Consider topic-invariant feature selection or normalization
  - Evaluate residual topic effects after stylometric analysis
- **LANGUAGE VARIATION": 
  - Mix of standard language, jargon, leetspeak, and dialectal variations
  - Need to handle informal, non-standard, and evolving language
  - Consider language-specific models or language-agnostic features
  - Evaluate code-switching and register shifting effects
  - Validate on multilingual authors if relevant to use case
- **INTENTIONAL OBFUSCATION": 
  - Sophisticated actors may deliberately alter their style
  - Test against known obfuscation techniques (manual or automated)
  - Evaluate effectiveness of style camouflage and mimicry
  - Consider uncertainty quantification for obfuscated texts
  - Develop features resistant to common obfuscation strategies
  - Combine with behavioral evidence to counteract style changes

### Implementation Approach for SIH26151

#### Feature Selection and Extraction Pipeline
- **PHASE 1: BASELINE FEATURES" 
  - Character n-grams (n=2-4) with TF-IDF weighting
  - Word n-grams (n=1-2, function words emphasized) with TF-IDF
  - Basic punctuation and whitespace features
  - Sentence length statistics (mean, variance)
  - Text length and basic readability metrics
- **PHASE 2: ENHANCED FEATURES" 
  - Part-of-speech n-grams (using lightweight tagger)
  - Syntactic features from shallow parsing
  - Readability and complexity metrics
  - Application-specific dark web communication features
  - Selected semantic features (topic proportions from LDA)
- **PHASE 3: ADVANCED FEATURES (if justified)": 
  - Contextual embeddings (sentence-transformers, USE)
  - Syntactic dependencies or constituency features
  - Advanced semantic features (word embeddings, semantic roles)
  - Complex structural features (discourse markers, narrative structure)
  - Learned feature representations (autoencoders, neural networks)

#### Model Selection Strategy
- **BASELINE MODEL": 
  - Linear SVM with character n-grams + TF-IDF (strong baseline)
  - Logistic regression with word and character features
  - Naive Bayes as computational efficiency baseline
- **ENHANCEMENT OPTIONS": 
  - Ensemble of multiple linear models (different feature sets)
  - Random Forest or XGBoost for non-linear interactions
  - Siamese network for direct similarity learning
  - Transformer-based classifier if sufficient data and justification
- **VALIDATION GATES": 
  - Must demonstrate improvement over character n-gram baseline
  - Must show reasonable performance on short texts (<50 words)
  - Must maintain precision above acceptable threshold (minimize false positives)
  - Must show reasonable topic independence (cross-topic validation)
  - Must provide uncertainty estimates or rejection option
- **UNCERTAINTY QUANTIFICATION": 
  - Probability calibration for score interpretation
  - Confidence thresholds for actionable predictions
  - Rejection interval for low-confidence cases requiring human review
  - Ensemble variance or Bayesian credible intervals
  - Document false positive rates at different confidence thresholds

#### Integration with Attribution Framework
- **OUTPUT FORMAT": 
  - Similarity score between 0 and 1 (1 = identical style)
  - Feature contribution breakdown (which features drove similarity)
  - Model version and parameter settings used
  - Processing time and resource consumption
  - Uncertainty estimate or confidence interval
  - Alternative explanations or confounding factors considered
- **INTERPRETATION GUIDANCE": 
  - Similarity scores require calibration to author pair likelihoods
  - Establish empirical distributions: same-author vs different-author scores
  - Set thresholds based on desired false positive rate
  - Provide likelihood ratios rather than binary decisions
  - Explain which specific stylistic elements contribute to similarity
  - Note limitations: short texts, topic effects, intentional obfuscation
- **ATTRIBUTION WEIGHTING": 
  - Stylometry evidence weight based on empirical false positive rate
  - Adjust for text length and number of samples compared
  - Consider temporal consistency of stylometric evidence
  - Discount if stylometry contradicted by stronger evidence types
  - Combine with other evidence using attribution confidence model

### Tools and Resources

#### Python Libraries
- **scikit-learn": 
  - Feature extraction: CountVectorizer, TfidfVectorizer
  - Classification: SVM, LogisticRegression, NaiveBayes, RandomForest
  - Utilities: train_test_split, cross_val_score, GridSearchCV
  - Metrics: accuracy_score, precision_score, f1_score, roc_auc_score
- **NLTK (Natural Language Toolkit)": 
  - Tokenization: word_tokenize, sent_tokenize
  - Part-of-speech tagging: pos_tag
  - Corpora: access to linguistic corpora for training data
  - Utilities: text processing, stemming, lemmatization
- **spaCy": 
  - Fast tokenization and part-of-speech tagging
  - Dependency parsing and named entity recognition
  - Word vectors and similarity
  - Pipeline customization for specific needs
  - Efficiency for processing large text volumes
- **gensim": 
  - Topic modeling: LDA, LS I, RP, HD P
  - Word embeddings: Word2Vec, FastText
  - Document similarity and indexing
  - Text summarization and retrieval
- **textstat": 
  - Readability metrics: Flesch-Kincaid, Gunning Fog, SMOG, etc.
  - Text complexity and grade level estimation
  - Multiple readability formulas for different purposes
  - Easy integration into feature extraction pipelines
- **pandas": 
  - Data manipulation and analysis
  - Feature storage and experimentation tracking
  - Time series handling for temporal stylometry
  - Integration with numerical computing workflows
- **numpy": 
  - Numerical computations for feature vectors
  - Linear algebra for similarity calculations
  - Random number generation for experiments
  - Foundation for scientific computing in Python

#### Specialized Stylometry Tools
- **JGAAP (Java Graphical Authorship Attribution Program)": 
  - GUI-based stylometric analysis suite
  - Multiple feature extractors and classifiers
  - Designed for authorship attribution and verification
  - Academic tool with documentation and examples
  - Java-based (platform independent but heavier than Python)
- **Stylo (R Package)": 
  - Comprehensive stylometry package for R
  - Multiple analytical methods and visualizations
  - Designed for literary and forensic stylometry
  - Active academic community and development
  - R-based (statistical strengths but different ecosystem)
- **authorship (Python Library)": 
  - Simple interface for authorship attribution tasks
  - Built-in datasets and evaluation methods
  - Focus on ease of use for common tasks
  - Active maintenance and community support
- **piroman (Authorship Attribution and Verification)": 
  - Focus on verification (same/different author decisions)
  - Multiple similarity measures and classifiers
  - Designed for forensic applications
  - Includes uncertainty quantification and threshold optimization

#### Corpora and Datasets for Training/Evaluation
- **PAN (Plagiarism Analysis, Authorship Identification, and Near-Duplicate Detection)": 
  - Annual competition with standardized authorship attribution tasks
  - Provides training and test corpora for various scenarios
  - Includes cross-domain, cross-topic, and obfuscation variations
  - Excellent resource for benchmarking and methodology development
  - Website: https://pan.webis.de/
- **ABCD (Attribution Benchmark Corpus for Dutch)": 
  - Dutch language authorship attribution corpus
  - Well-documented with known authorship ground truth
  - Includes various text lengths and genres
  - Useful for language-specific validation and methodology testing
- **Federalist Papers Corpus": 
  - Classic authorship attribution dataset (Hamilton, Madison, Jay)
  - Extensively studied in stylometry literature
  - Good for validating basic methodologies and assumptions
  - Historical texts with established scholarly consensus
- **Enron Email Corpus": 
  - Real-world corporate email collection with known authors
  - Extensively used for stylometry and social network analysis
  - Includes temporal dynamics and relationship information
  - Requires careful handling due to privacy considerations
  - Website: https://www.cs.cmu.edu/~./enron/
- **Blog Authorship Corpus": 
  - Collection of blog posts with known authors
  - Designed specifically for authorship attribution research
  - Includes temporal variations and topic diversity
  - Large scale (19,320 posts by 10,000 authors)
  - Website: https://www.cs.utexas.edu/users/ml/badrcorpus.html

#### Computational Considerations
- **FEATURE EXTRACTION EFFICIENCY": 
  - Pre-compile regular expressions for performance
  - Use vectorized operations where possible (numpy, pandas)
  - Consider streaming processing for very large corpora
  - Cache intermediate results for repeated use
  - Profile extraction pipeline to identify bottlenecks
- **MODEL TRAINING AND INFERENCE": 
  - Start with linear models for speed and interpretability
  - Consider approximate nearest neighbors for large databases
  - Implement incremental learning if updating with new samples
  - Use model serialization for persistence and reuse
  - Profile inference latency for real-time or interactive use
- **MEMORY AND STORAGE": 
  - Sparse representations for high-dimensional feature matrices
  - Feature selection to reduce dimensionality
  - Consider hashing trick for memory-efficient feature encoding
  - Database storage for feature vectors and metadata
  - Compression techniques for archival storage
- **PARALLELIZATION AND DISTRIBUTION": 
  - Parallel feature extraction across documents or features
  - Distributed model training for large datasets
  - Caching layers for frequent similarity computations
  - Asynchronous processing for non-interactive tasks
  - Load balancing for handling variable workloads

### Limitations and Mitigation Strategies

#### Known Limitations of Stylometry
- **SHORT TEXT SENSITIVITY": 
  - MITIGATION: 
    * Combine multiple short texts from same author
    * Use character n-grams which work better on short text
    * Increase required similarity threshold for short texts
    * Consider behavioral and infrastructure evidence as primary
    * Validate effectiveness on expected text lengths
- **TOPIC AND GENER DEPENDENCE": 
  - MITIGATION: 
    * Use function words and character n-grams (less topic dependent)
    * Apply topic modeling and residual analysis
    * Validate cross-topic performance explicitly
    * Combine with topic-independent evidence sources
    * Develop topic normalization techniques
- **STYLE DRIFT AND EVOLUTION": 
  - MITIGATION: 
    * Model style as evolving distribution rather than fixed point
    * Use temporal windows for comparison
    * Incorporate time-dependent similarity functions
    * Validate on known style changes (education, career shifts)
    * Combine with behavioral evidence that may change less
- **INTENTIONAL OBFUSCATION": 
  - MITIGATION: 
    * Test against known obfuscation techniques
    * Develop features resistant to common obfuscation
    * Combine with evidence harder to obfuscate (infrastructure, behavior)
    * Use uncertainty quantification to flag suspicious cases
    * Consider multimodal analysis (style + behavior + infrastructure)
- **FALSE POSITIVES FROM COMMON TRAITS": 
  - MITIGATION: 
    * Establish empirical false positive rates from background populations
    * Apply specificity weighting based on population prevalence
    * Require convergence of multiple evidence types
    * Use likelihood ratios rather than raw similarity scores
    * Implement rejection criteria for low-confidence cases
- **LANGUAGE AND DIALECT VARIATION": 
  - MITIGATION: 
    * Use language-specific models when sufficient data
    * Consider language-agnostic features (character level)
    * Normalize for dialectal variations where possible
    * Validate on relevant language variants
    * Consider multilingual models or ensemble approaches

#### Operational Guidelines for Investigators
- **INTERPRETING STYLOMETRY OUTPUTS": 
  - Never treat similarity score as probability of authorship
  - Always consider false positive rate and base rates
  - Look for convergence with other evidence types
  - Consider alternative explanations for similarity
  - Document limitations and uncertainties in reports
  - Use as investigative lead rather than conclusive proof
- **WHEN TO TRUST STYLOMETRY RESULTS": 
  - High similarity scores on substantial text samples
  - Convergence with independent evidence (behavioral, infrastructure)
  - Consistency across multiple text samples from same period
  - Low false positive rate in validation on similar materials
  - Expert review confirms face validity and plausibility
  - Clear explanation of which specific stylistic elements match
- **WHEN TO BE SKEPTICAL": 
  - Very short texts or single samples
  - High topic specificity with no cross-topic validation
  - Known or suspected attempts at style obfuscation
  - Conflicts with stronger evidence types (direct identifiers)
  - Lack of validation on similar materials or contexts
  - Unexplained high similarity without clear feature explanation
  - Results that contradict investigative expectations without explanation
- **COMBINING WITH OTHER EVIDENCE": 
  - Use stylometry to generate hypotheses for investigation
  - Prioritize infrastructure and direct evidence for confirmation
  - Use behavioral evidence to check for consistency over time
  - Consider stylometry as one thread in convergent evidence
  - Apply attribution confidence model for principled combination
  - Allow for stylometry to be outweighed by stronger evidence

This stylometry methodology provides a scientifically grounded approach to authorship attribution that emphasizes validation, uncertainty quantification, and integration with broader attribution frameworks rather than promising infallible author identification.