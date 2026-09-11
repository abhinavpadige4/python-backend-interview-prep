# System Design Basics for Backend Interviews

## 🏗️ Core System Design Concepts

### Scalability
**Definition**: Ability of a system to handle growing amounts of work by adding resources.

**Types**:
- **Vertical Scaling (Scaling Up)**: Adding more power (CPU, RAM) to existing machine
- **Horizontal Scaling (Scaling Out)**: Adding more machines to the system

**Techniques**:
- Load balancing
- Database sharding
- Caching
- Asynchronous processing
- Microservices

### Availability & Reliability
**Availability**: Percentage of time system is operational and accessible
- **Uptime SLA**: 99.9% = ~8.76 hours downtime/year
- **Five Nines**: 99.999% = ~5.26 minutes downtime/year

**Reliability**: Probability that system will perform its intended function without failure

**Techniques**:
- Redundancy
- Failover mechanisms
- Health checks
- Circuit breakers
- Graceful degradation

### Consistency Models
**CAP Theorem**: In distributed systems, you can only have two of three:
- **Consistency**: All nodes see same data at same time
- **Availability**: Every request receives response
- **Partition Tolerance**: System continues despite network partitions

**Consistency Levels**:
- **Strong Consistency**: Immediate consistency across all nodes
- **Eventual Consistency**: Consistency achieved after some time
- **Causal Consistency**: Preserves cause-effect relationships
- **Read-After-Write Consistency**: User sees their own writes immediately

### Latency & Throughput
- **Latency**: Time to process single request (response time)
- **Throughput**: Number of requests processed per unit time
- **Relationship**: Often inverse - optimizing one may affect the other

## 🔧 Key System Components

### Load Balancer
**Purpose**: Distribute incoming network traffic across multiple servers

**Types**:
- **Layer 4 (Transport)**: Works with TCP/UDP packets
- **Layer 7 (Application)**: Works with HTTP requests (can inspect content)

**Algorithms**:
- Round Robin
- Least Connections
- IP Hash
- Least Response Time
- Weighted variants

**Features**:
- Health checks
- SSL termination
- Session persistence (sticky sessions)
- HTTP/2 support

### Database
**Relational Databases (SQL)**:
- ACID properties
- Structured data with schemas
- Examples: MySQL, PostgreSQL, Oracle, SQL Server
- Vertical scaling typical
- Joins and complex queries

**NoSQL Databases**:
- Flexible schema
- Horizontal scaling
- Examples: MongoDB (document), Cassandra (wide-column), Redis (key-value), Neo4j (graph)
- Eventual consistency common
- Optimized for specific access patterns

**Database Patterns**:
- **Master-Slave Replication**: Writes to master, reads from slaves
- **Master-Master Replication**: Writes to any node
- **Sharding**: Partition data across multiple databases
- **Read Replicas**: Offload read queries
- **Connection Pooling**: Reuse database connections

### Caching
**Purpose**: Store frequently accessed data in fast memory to reduce latency

**Types**:
- **Client-side**: Browser caching, CDN
- **Server-side**: In-memory caches (Redis, Memcached)
- **Database-level**: Query result caching
- **Application-level**: Object caching

**Cache Strategies**:
- **Cache Aside (Lazy Loading)**: Load data into cache on cache miss
- **Write Through**: Write to cache and database simultaneously
- **Write Behind (Write Back)**: Write to cache first, then to database asynchronously
- **Refresh Ahead**: Proactively refresh cache before expiration

**Cache Eviction Policies**:
- LRU (Least Recently Used)
- LFU (Least Frequently Used)
- FIFO (First In, First Out)
- Random
- TTL (Time To Live)

### Message Queues
**Purpose**: Enable asynchronous communication between services

**Patterns**:
- **Point-to-Point**: One producer, one consumer
- **Publish/Subscribe**: One producer, multiple consumers
- **Request/Reply**: Synchronous-like behavior over async

**Popular Solutions**:
- RabbitMQ
- Apache Kafka
- Amazon SQS
- Redis Pub/Sub
- Apache Pulsar

**Use Cases**:
- Decoupling services
- Buffering traffic spikes
- Workload distribution
- Event-driven architectures
- Reliability and retry mechanisms

## 🌐 API Design Principles

### RESTful API Design
**Resources**: Nouns representing entities (not verbs)
- Good: `/users`, `/orders`, `/products`
- Avoid: `/getUsers`, `/createOrder`, `/deleteProduct`

**HTTP Methods**:
- **GET**: Retrieve resource (safe, idempotent)
- **POST**: Create new resource (not idempotent)
- **PUT**: Update/replace resource (idempotent)
- **PATCH**: Partially update resource (not necessarily idempotent)
- **DELETE**: Remove resource (idempotent)

**Status Codes**:
- **2xx Success**: 200 OK, 201 Created, 204 No Content
- **3xx Redirection**: 301 Moved Permanently, 304 Not Modified
- **4xx Client Error**: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests
- **5xx Server Error**: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout

**Best Practices**:
- Use nouns, not verbs in endpoints
- Use HTTP methods correctly
- Return appropriate status codes
- Use JSON for request/response bodies
- Version your API (`/v1/users`)
- Use plural nouns for collections
- Use nesting for relationships (`/users/123/orders`)
- Implement pagination, filtering, sorting
- Provide clear error messages
- Use HTTPS for security
- Implement rate limiting
- Document your API (OpenAPI/Swagger)

### GraphQL Basics
**Concept**: Query language for APIs that allows clients to request exactly what they need

**Key Features**:
- Single endpoint (`/graphql`)
- Client specifies exact data needed
- Strongly typed schema
- Introspection capabilities
- Real-time updates with subscriptions

**Advantages over REST**:
- No over-fetching or under-fetching
- Evolves without versioning
- Better developer experience
- Efficient data fetching

### API Security
- **Authentication**: Verify identity (API keys, JWT, OAuth)
- **Authorization**: Check permissions (RBAC, ABAC)
- **Input Validation**: Prevent injection attacks
- **Rate Limiting**: Prevent abuse
- **Encryption**: HTTPS/TLS for data in transit
- **CORS**: Control cross-origin requests
- **Security Headers**: CSP, HSTS, X-Frame-Options

## 📊 Data Storage & Management

### Database Design
**Normalization**:
- **1NF**: Atomic values, no repeating groups
- **2NF**: Meet 1NF and no partial dependencies
- **3NF**: Meet 2NF and no transitive dependencies
- **BCNF**: Stronger version of 3NF

**Denormalization**: Intentional redundancy for performance
- Read-heavy applications
- Complex joins expensive
- Reporting and analytics

**Indexing**:
- **B-Tree**: Default for most databases
- **Hash**: Equality lookups
- **GiST/GIN**: PostgreSQL for full-text search
- **Full-text**: Text search capabilities

**Partitioning**:
- **Horizontal (Sharding)**: Split rows across tables
- **Vertical**: Split columns across tables
- **Range**: Based on value ranges
- **List**: Based on discrete values
- **Hash**: Based on hash function

### Caching Strategies
**Cache Layers**:
- **CPU Registers**: Fastest, smallest
- **CPU Cache**: L1, L2, L3 caches
- **Main Memory**: RAM
- **SSD/NVMe**: Fast storage
- **HDD**: Slow storage
- **Network**: Remote caches

**Cache Invalidation**:
- **Time-based**: TTL expiration
- **Event-based**: Invalidate on data change
- **Manual**: Administrative invalidation
- **Query-based**: Invalidate based on queries

## 🔄 Concurrency & Parallelism

### Threading vs Multiprocessing
**Threading**:
- Shared memory space
- Lightweight context switching
- GIL limits true parallelism in Python (CPU-bound)
- Good for I/O-bound tasks
- Race conditions possible

**Multiprocessing**:
- Separate memory spaces
- True parallelism (multiple cores)
- Higher memory overhead
- Inter-process communication needed
- Good for CPU-bound tasks

### AsyncIO
**Concept**: Single-threaded concurrent code using coroutines

**Key Elements**:
- **Event Loop**: Manages execution of coroutines
- **Coroutines**: Functions that can be paused/resumed (`async def`)
- **Tasks**: Wrapped coroutines scheduled for execution
- **Futures**: Low-level awaitable objects
- **Await**: Pause coroutine until awaitable completes

**Use Cases**:
- High-concurrency I/O (web servers, APIs)
- Network programming
- File operations
- Database connections
- Web scraping

### Synchronization Primitives
**Locks/Mutexes**: Ensure exclusive access to shared resource
**Semaphores**: Limit number of concurrent accesses
**Conditions**: Wait for specific condition to become true
**Events**: Signal between threads
**Barriers**: Make threads wait until all reach certain point
**Queues**: Thread-safe data structures for producer-consumer

## 📈 Monitoring & Observability

### Logging
**Levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL
**Structured Logging**: JSON format for easier parsing
**Log Rotation**: Prevent disk space exhaustion
**Centralized Logging**: ELK stack, Splunk, Datadog

### Metrics
**Types**:
- **Counters**: Monotonically increasing (requests served)
- **Gauges**: Instantaneous values (memory usage)
- **Histograms**: Distribution of values (response times)
- **Summaries**: Similar to histograms with quantiles

**Collection**: Prometheus, StatsD
**Visualization**: Grafana, Kibana

### Tracing
**Distributed Tracking**: Follow request across services
**Span**: Unit of work in trace
**Trace ID**: Unique identifier for entire request
**Span ID**: Identifier for individual span
**Parent-Child Relationships**: Show call hierarchy

**Tools**: Jaeger, Zipkin, AWS X-Ray, OpenTelemetry

### Health Checks
**Liveness Probe**: Is application running?
**Readiness Probe**: Is application ready to serve traffic?
**Startup Probe**: Has application finished starting?

## 🔒 Security Fundamentals

### Authentication
**Methods**:
- **Password-based**: Username/password
- **Token-based**: JWT, API keys
- **OAuth**: Delegated authorization
- **OpenID Connect**: Identity layer on OAuth
- **Certificates**: Mutual TLS
- **Biometrics**: Fingerprint, face recognition
- **Multi-factor**: Combination of above

### Authorization
**Models**:
- **RBAC**: Role-Based Access Control
- **ABAC**: Attribute-Based Access Control
- **PBAC**: Policy-Based Access Control
- **ACL**: Access Control Lists

### Common Vulnerabilities
- **Injection**: SQL, NoSQL, Command, XSS
- **Broken Authentication**: Session management, credential stuffing
- **Sensitive Data Exposure**: Encryption, hashing
- **XML External Entities (XXE)**: File disclosure, SSRF
- **Broken Access Control**: Privilege escalation
- **Security Misconfiguration**: Default configs, unnecessary features
- **Cross-Site Scripting (XSS)**: Stored, reflected, DOM-based
- **Insecure Deserialization**: Remote code execution
- **Using Components with Known Vulnerabilities**: Outdated libraries
- **Insufficient Logging & Monitoring**: Lack of attack detection

### Best Practices
- **Principle of Least Privilege**: Minimum permissions needed
- **Defense in Depth**: Multiple layers of security
- **Input Validation**: Whitelist vs blacklist
- **Output Encoding**: Prevent XSS
- **Password Hashing**: bcrypt, scrypt, PBKDF2
- **Secrets Management**: Environment variables, vaults
- **Regular Updates**: Patch management
- **Security Testing**: SAST, DAST, penetration testing
- **Encryption**: AES, RSA, TLS
- **Network Security**: Firewalls, IDS/IPS, VPN

## 🚀 Deployment & DevOps

### CI/CD Pipeline
**Continuous Integration**: Automated build and test
**Continuous Delivery**: Automated release to staging
**Continuous Deployment**: Automated release to production

**Stages**:
1. Code commit
2. Build/compile
3. Automated testing (unit, integration, UI)
4. Security scanning
5. Deploy to staging
6. Performance testing
7. Deploy to production
8. Monitoring and rollback

**Tools**: Jenkins, GitLab CI, GitHub Actions, CircleCI, Travis CI

### Containerization
**Docker**:
- Package application with dependencies
- Consistent environments
- Isolation and resource limits
- Image layers for efficient storage

**Kubernetes**:
- Orchestration platform for containers
- Auto-scaling, self-healing
- Service discovery and load balancing
- Rolling updates and rollbacks
- Configuration and secrets management

### Infrastructure as Code (IaC)
**Concept**: Manage infrastructure through machine-readable files

**Benefits**:
- Version control
- Reproducibility
- Consistency
- Auditability
- Automation

**Tools**: Terraform, AWS CloudFormation, Azure Resource Manager, Ansible

### Blue-Green Deployment
**Strategy**: Two identical production environments
- **Blue**: Current live version
- **Green**: New version being tested
- Switch router to direct traffic to green when ready
- Quick rollback capability

### Canary Release
**Strategy**: Gradually roll out to subset of users
- Small percentage (e.g., 5%) get new version
- Monitor metrics and feedback
- Gradually increase percentage
- Full rollout if successful

## 🎯 Interview Preparation Tips

### System Design Interview Process
1. **Clarify Requirements**: Ask about scale, features, constraints
2. **Define Scope**: What's in/out of scope
3. **High-Level Design**: Core components and interactions
4. **Detailed Design**: Drill into critical components
5. **Identify Bottlenecks**: Where will system struggle?
6. **Address Concerns**: Scalability, availability, consistency
7. **Consider Trade-offs**: What are we sacrificing?

### Common System Design Questions
- Design URL shortener (like bit.ly)
- Design Twitter/X
- Design Instagram/Pinterest
- Design Chat application (like WhatsApp)
- Design Video streaming service (like YouTube/Netflix)
- Design Ride-sharing app (like Uber/Lyft)
- Design Search engine (like Google)
- Design File sharing service (like Dropbox)
- Design Rate limiter
- Design Web crawler
- Design Recommendation system
- Design Ticketing system (like Ticketmaster)

### Key Metrics to Consider
- **QPS**: Queries Per Second
- **DAU/MAU**: Daily/Monthly Active Users
- **Peak vs Average Traffic**
- **Read/Write Ratio**
- **Data Size and Growth Rate**
- **Latency Requirements (P50, P95, P99)**
- **Availability Requirements**
- **Consistency Requirements**

### Trade-off Framework
- **Performance vs Cost**
- **Consistency vs Availability**
- **Latency vs Throughput**
- **Simplicity vs Flexibility**
- **Development Speed vs Maintenance**
- **Feature Richness vs Time to Market**

### Documentation & Communication
- **Draw clear diagrams**: Components, data flow, interactions
- **Explain your thinking**: Why you chose certain approaches
- **Consider edge cases**: What happens when things fail?
- **Discuss alternatives**: What other approaches did you consider?
- **Quantify your decisions**: Estimates for QPS, storage, costs