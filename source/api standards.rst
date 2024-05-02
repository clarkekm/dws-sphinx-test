API Standards
=====================================

Clients integrating a range of Morningstar APIs expect a consistent experience. Common technical and documentation standards enable us to deliver that experience to our end users.:: 

Examples used in the documentation are based on endpoints, resources, and parameters that you will be familiar with from existing Morningstar APIs. Names have been modified where necessary to demonstrate best practice.


Resources
***********************************

"Resources" refer to the categories or collections of information returned by an API.

* [Overview](#resource-overview-id)
* [Technical Standards](#resource-tech-standards-id)
* [Documentation Standards](#resource-docs-standards-id)


Overview
--------------------------------------

Resources can be a collection or a singleton.

|Type|Description|Example|
|:------|:------|:----|
|Collection |A collection of homogenous resources. MAY contain sub-collection resources.|`securities`, `models`, `portfolios`, `companies`. |
|Singleton| A singleton resource that points to a specific resource within a collection. Singleton resources are variable parts of the URI path as they are substituted with an actual value when you make an API call.| `security`, `model`, `portfolio`, `company`.|

When you define relationships between resources, you can create paths (endpoints) to various types of information.

Return **all** securities:
````
GET /securities
````
\
Return a **single** security:
````
GET /securities/{securityId}
```` 
\
Return **all** portfolios associated with the security specified:
````
GET /securities/{securityId}/portfolios
````
\
Return a **single** portfolio associated with the security specified:
````
GET /securities/{securityId}/portfolios/{portfolioId}
```` 
\
When we document APIs in the [OpenAPI Specification (OAS)](/apis/getting-started/api-standards/latest/documentation-oas), we group endpoints by tagging them with the name of the top-level resource. 

In the following example, there are four endpoints that return information about the `securities` resource. (`securities` is also an endpoint as it is a path to resource information.)

````
GET /securities
GET /securities/{securityId}
GET /securities/{securityId}/portfolios
GET /securities/{securityId}/portfolios/{portfolioId}

````

Technical Standards
------------------------


* Identify all resources - collection resources and singleton resources.
* Define the relationships between resources.
* Define the machine-readable format to represent each resource.
* Use JSON (application/json) or XML (application/xml) to represent resources.
* Use curly brackets {} to set off singleton resources in the URI.
* Granularity:
  * MAY  be decided based on cacheablility, frequency of change, mutability.
  * SHOULD ensure a good grade of cacheability and stability.

Documentation Standards
-------------------------------------

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

|Standard|Example|
|:----|:-----|
|Use plural nouns to name collection resources.|`securities`, `research-reports`, `questionnaires`|
|Use verbs **if and only if** the resource is an operation.|`calculate-total-return-index`|
|Use hyphens to separate multi-word resources.|`research-reports`, `portfolio-analytics`|
|Resources MUST be lower-case in the URI. (Does not apply to singleton resources which are variables.)|`research-reports`, `portfolio-analytics`|
|Do not abbreviate/truncate words.|Use `questionnaires` not `quests`|
|Avoid acronyms except for those accepted as industry standards.|`esg-questionnaires`|

