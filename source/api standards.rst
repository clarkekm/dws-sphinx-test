# API Technical Standards v1.0 - DRAFT

Clients integrating a range of Morningstar APIs expect a consistent experience. Common technical and documentation standards enable us to deliver that experience to our end users. 

>Examples used in the documentation are based on endpoints, resources, and parameters that you will be familiar with from existing Morningstar APIs. Names have been modified where necessary to demonstrate best practice.

* [Resources](#resources-id)
* [URIs](#uris-id)
* [Versioning](#versions-id)
* [Query Strings](#query-id)
* [HTTP Methods](#http-methods-id)
* [HTTP Status Codes and Error Messages](#codes-id)
* [Internationalization and Localization](#international-id)
* [Content Negotiation](#content-negotiation-id)
* [Output Format](#output-id)
* [Tracing and Logging](#tracing-id)
* [Caching](#caching-id)
* [Documentation]()

## Resources {#resources-id}

"Resources" refer to the categories or collections of information returned by an API.

* [Overview](#resource-overview-id)
* [Technical Standards](#resource-tech-standards-id)
* [Documentation Standards](#resource-docs-standards-id)


### Overview {#resource-overview-id}

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

  
### Technical Standards {#resource-tech-standards-id}


* Identify all resources - collection resources and singleton resources.
* Define the relationships between resources.
* Define the machine-readable format to represent each resource.
* Use JSON (application/json) or XML (application/xml) to represent resources.
* Use curly brackets {} to set off singleton resources in the URI.
* Granularity:
  * MAY  be decided based on cacheablility, frequency of change, mutability.
  * SHOULD ensure a good grade of cacheability and stability.

### Documentation Standards {#resource-docs-standards-id}

|Standard|Example|
|:----|:-----|
|Use plural nouns to name collection resources.|`securities`, `research-reports`, `questionnaires`|
|Use verbs **if and only if** the resource is an operation.|`calculate-total-return-index`|
|Use hyphens to separate multi-word resources.|`research-reports`, `portfolio-analytics`|
|Resources MUST be lower-case in the URI. (Does not apply to singleton resources which are variables.)|`research-reports`, `portfolio-analytics`|
|Do not abbreviate/truncate words.|Use `questionnaires` not `quests`|
|Avoid acronyms except for those accepted as industry standards.|`esg-questionnaires`|

## URIs {#uris-id}

>`[scheme]://[host]/[`**URI**`]?[query string]`


URI stands for "Uniform Resource Identifier". Each API [resource](#resources-id) has at least one URI. 

* [Design Standards](#uri-design-id)
* [Technical Standards](#uri-tech-standards-id)
* [Documentation Standards](#uri-docs-standards-id)


### Design Standards {#uri-design-id}

>URI design MUST be based on **stable** concepts, identifiers, and information.

You MUST consider **readability** when designing URIs. 

Consider this example:

````
[scheme+host]/rs/quests/riskquests/[query string]

````  
\
Unless you are already familiar with the API, this URI is confusing:

* What does `rs` stand for? Risk survey, risk stratification, risk size?
* `quests` probably means `questions` or `questionnaires`, but it's not clear.
* Is `riskquests` a typo? Should it be `requests`? Or is it an abbreviation?
* What is the API version?

\
Compare the previous URI with this one:

````

[scheme+host]/risk-score/v1/questionnaires/risk-questionnaires/[query string]

```` 
\
Even if you are unfamiliar with the API, you can understand a lot about the request just from reading the URI:

* The URI identifies the Risk Score API's `questionnaires` resource.
* This is version 1 of the API. 
* A call to the URI returns information about the risk questionnaire(s).
* As `risk-questionnaires` is a sub-collection of `questionnaires`, we can assume that there are other categories of questionnaires.


\
**Examples**

````
https://www.us-api.morningstar.com/enterprise-components/v1/securities
https://www.us-api.morningstar.com/risk-models/v2/models/{riskModelId}
https://www.us-api.morningstar.com/portfolio-analytics/v1/xrays/views/{viewId}
https://www.us-api.morningstar.com/report-retrieval/v1/reports/{reportId}

````

### Technical Standards {#uri-tech-standards-id}

The basic structure of a URI is:

>`/[api-name]/[version]/[resource]`


|Standard|Example|
|:----|:-----|
|1st segment MUST be the API name.| `enterprise-components`, `risk-models`|
|2nd segment MUST be a [version number](#versions-id).|`v1`, `v2`|
|3rd segment MUST be a [resource](#resources-id).|`models`, `securities`, `investment-profiles`|
|Use forward slash (/) to indicate hierarchical relationship between resources.|`.../reports​/global-fund-report​/`|
|Use hyphens to delimit words. Do not use spaces.|`portfolio-analytics`,`risk-questionnaires`|
|If a change to the URI is mandated, use status code 300 for redirection.||


### Documentation Standards {#uri-docs-standards-id}

|Standard|Example|
|:----|:-----|
|MUST be lower-case.|`/enterprise-components/v1/securities/`|
|Default language is English.||
|Do not use special characters.||
|Use hyphens to separate words.|`.../reports/global-fund-reports`|
|Avoid abbreviations where possible.|Avoid `.../pa/v1`, use `/portfolio-analytics/v1`|

## Versioning {#versions-id}

Versioning enables users to easily track and identify changes in an API. 

* [General Standards](#version-general-id)
* [Technical Standards](#version-tech-standards-id)

### General Standards {#version-general-id}

* APIs MUST have a version number.
* You MUST introduce a new version when the server is unable to maintain backward compatibility.
* You MUST maintain APIs at least one version back.

### Technical Standards {#version-tech-standards-id}

|Applies To|Standard|Examples|
|:-----|:-----|:-----|
|Format|Use semantic versioning.|www.semver.org|
|URI|You MUST specify version in the [URI](/apis/getting-started/api-standards/latest/uris).|`/v{version}/{resource}` |
||Versions MUST be an integer that refers to the major version and is prefixed with ‘v’.| `/v1/{risk-models}`|

## Query Strings {#query-id}

>`[scheme]://[host]/[URI]?[`**query string**`]`

Query string parameters are `key=value` pairs that appear after a question mark (`?`) in the endpoint. 

* [Technical Standards](#query-tech-standards-id)
  * [General](#query-general-id)
  * [Selection](#selection-id)
  * [Projection](#projection-id)
  * [Sorting and Ordering](#sort-id)
  * [Pagination](#pagination-id)


### Technical Standards {#query-tech-standards-id}

> Query string parameters follow the JavaScript **camelCase** naming convention for variables.

#### General {#query-general-id}

* Separate query string parameters with ampersands (`&`).
* The order of the query string parameters is not important.



#### Selection {#selection-id}

Use selection to query rows (individual records) in the database. 

* Use to reduce the number of records queried by specifying attributes and their expected values.
* You can filter on several attributes in the same request.
* You can specify several values for a single filter.

For example, the following request returns all information about the 2 securities specified.

````
GET [server+host+uri]?securityId=FOUSA06N2B|FEUSA04ABV

````
\
This request returns a subset of information about the 2 securities queried.

````
GET [server+host+uri]?securityId=FOUSA06N2B|FEUSA04ABV&dataPoints=name|cusip|ticker|category

````

#### Projection {#projection-id}

Use projection to query columns (fields) in the database. 

* You can filter on several fields in the same request.
* You can use a predefined view.

````
GET [server+host+uri]?fields=isin,legalName,closePrice
GET [server+host+uri]?view={viewId}

````

#### Sorting and Ordering {#sort-id}

* The `sort` parameter contains the comma-separated names of the attributes on which the sorting is performed.
* The `order` parameter defines the order of the sorted values.
* Possible `order` values are `desc` (descending) and `asc` (ascending.)
* The default `order` value should be descending (`desc`).

````
[server+host+uri]?securityId=FOUSA06N2B|FEUSA04ABV&ataPoints=name|cusip|ticker|category&sort=name,cusip&order=desc

````


#### Pagination {#pagination-id}

Use pagination to make responses easier to handle.

* Use `limit` to specify the number of results per request.
* Use `skip` to specify the number of results to skip.
* Response should include the total number of results possible so that the user can determine if there are more pages.
* Use a link header to return a set of ready-made links so the user does not have to construct links themselves. This is especially valuable when pagination is cursor-based.

## HTTP Methods {#http-methods-id}

Methods indicate the allowed interactions with a resource.
\

* [Technical Standards](#methods-tech-standards-id)
  * [GET](#get-id)
  * [POST](#post-id)
  * [PUT](#put-id)
  * [PATCH](#patch-id)
  * [DELETE](#delete-id)
* [Documentation Standards](#methods-docs-standards-id)


### Technical Standards {#methods-tech-standards-id}

A method can have the following characteristics:

|Characteristic|Description|
|:----|:-----|
|SAFE| Does not change the resource.|
|NON SAFE| MAY change the resource.|
|IDEMPOTENT|Output remains the same.|
|NON-IDEMPOTENT|Output MAY vary if same request is issued multiple times| 

### GET {#get-id}

* Use to retrieves a representation of a resource.
* SAFE - Changes MUST NOT be applied to the resource. 
* NON-IDEMPOTENT - Output MAY vary if same request is issued multiple times. 

\
**Request**

```
curl --request GET \
  --url https://{www.example.com}/{api-name}/{version}/{resource}

```
\
**Response**

```
HTTP/1.1 200 OK
Location: https://{www.example.com}/{api-name}/{version}/{resource}/12345
Content-Length: xxx

{"name":"ABCo", "content":"XYZ"}

```

### POST {#post-id}

* Use to create a new resource.
* NOT SAFE - MAY change the value of the resource. 
* NON-IDEMPOTENT - Output MAY vary if same request is issued  multiple times. 

\
**Request**

```
curl --request POST \
  --url https://{www.example.com}/{api-name}/{version}/{resource} \
  --header 'content-type: application/json' \
  --data '{"name":"ABCo", "content":"XYZ"}'

```
\
**Response**

````
HTTP/1.1 201 Created
Location: https://{www.example.com}/{api-name}/{version}/{resource}/12345
Content-Length: xxx

{"id": 12345, "name":"ABCo", "content":"XYZ", "_media": {"links": [{"ref": "/api/resource/12345", "rel": "self"}]}}

````

### PUT {#put-id}

* Use to update a resource.
* You MUST specify an identifier for the resource.
* NON SAFE - MAY change the value of the resource.
* IDEMPOTENT - Returns the same output if same request is issued multiple times. 

\
**Request**


```
curl --request PUT \
  --url https://{www.example.com}/{api-name}/{version}/{resource}{{id}} \
  --header 'content-type: application/json' \
  --data '{"name":"ABCo", "content":"XYZ"}'

```
\
**Response**

```
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 123

```

### PATCH {#patch-id}

* Use to update part of an existing resource.
* NON SAFE - MAY change the value of the resource. 
* NON-IDEMPOTENT - MAY NOT return the same output if same request is issued multiple times.


\
**PATCH Request - Replace or add value to a singleton resource**

```
curl --request PATCH \
  --url https://{www.example.com}/{api-name}/{version}/{resource}/{{id}} \
  --header 'content-type: application/json' \
  --data '{"field": "name", "value": "ABCo"}'

```
\
**PATCH Request - Remove field from a singleton resource**

```
curl --request PATCH \
  --url https://{www.example.com}/{api-name}/{version}/{resource}/{{id}} \
  --header 'content-type: application/json' \
  --data '[{"field": "name", "action": "DELETE"}]'

```
\
**PATCH Request - Add elements to an array**

```
curl --request PATCH \
  --url https://{www.example.com}/{api-name}/{version}/{resource}/{{id}} \
  --header 'content-type: application/json' \
  --data '[{"field": "keywords", "value": ["5", "stars"], "action": "INSERT"}]'

```
\
**PATCH Request - Replace element**

```
curl --request PATCH \
  --url https://{www.example.com}/{api-name}/{version}/{resource}/{{id}} \
  --header 'content-type: application/json' \
  --data '[{"field": "keywords", "value": ["5"], "action": "DELETE"}{"field": "keywords", "value": ["4"], "action": "INSERT"}]'

```
\
**Response**

```
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 0
Body: (null)

```

### DELETE {#delete-id}

* Use to delete a resource.
* NON SAFE - Deletes a resource.
* IDEMPOTENT - MUST return the same output if same request is issued multiple times.

\
**Request**


````
curl --request DELETE \
  --url https://{www.example.com}/{api-name}/{version}/{resource}/{{id}}

````
\
**Response**

````
HTTP/1.1 204 No Content
Content-Type: application/json
Content-Length: 0
Body: (null)

````


### Documentation Standards {#methods-docs-standards-id}

When you document an endpoint, start with a verb that describes the action initiated by the method:

|Method|Suggested Verbs|
|:----|:-----|
|GET|Get..., Retrieve..., |
|PUT|Update..., Create... (used with an existing resource)|
|POST|Create...|
|PATCH|Update...|
|DELETE|Delete... Remove...|

## Internationalization and Localization {#international-id}

"Internationalization" and "localization" refer to the ways we adapt computer software to different languages, regional differences, and the technical requirements of a target market. 

As Morningstar is a global company, all APIs **MUST** be designed with internationalization and localization in mind.

* [Locales](#locales-id)
* [Accept-Language Header](#accept-id)
* [Content-Language Representation Header](#content-id)

### Locales {#locales-id}

* A "locale" specifies the regional variation of a language. For example, `fr-FR` specifies the French language as spoken in France, `ca-FR` specifies Canadian French. 
* Valid language identifier for a locale is any [two-letter ISO-639 language code](https://www.iso.org/standard/22109.html). For example, `en`, `fr`
* Valid country identifier for a locale is any [two-letter ISO-3166 country code](https://www.iso.org/iso-3166-country-codes.html). For example, `US`, `FR`
* To support localization, you MUST use locales (for example, `fr-CA`) as a language code (for example, `fr`) does not allow for regional variations.


### Accept-Language Header {#accept-id}
* APIs MUST support the `Accept-Language` HTTP request header to indicate the locale.
* APIs MAY allow users to override locale in the `Accept-Language` header by specifying the locale in a query string parameter in the URL.
* If the locale query string parameter is specified, the `Accept-Language` header MUST be ignored.
* If the requested locale cannot be satisfied by the API, the API MUST return a HTTP `400 Bad Request` error.
* APIs MAY choose to support language ranges with associated quality values in order to better support localization. For example, the following values in the mean "I prefer Danish, but will accept British English and other types of English." -   `Accept-Language: da, en-gb;q=0.8, en;q=0.7`


### Content-Language Representation Header {#content-id}
* API MUST send the `Content-Language` representation header in the response to indicate the language of the response content. For example, `Content-Language: da`.
* Use a [two-letter ISO-639 language code](https://www.iso.org/standard/22109.html). For example, `en`, `fr`

## Content Negotiation {#content-negotiation-id}

"Content negotiation" is the process of selecting the best representation for a response when there are multiple representations available. The information included in a response might be represented in different formats, languages or encodings.

For detailed information about this topic see the [www.w3.org](http://www.w3.org/Protocols/rfc2616/rfc2616-sec12.html) website and the [Content Negotiation](http://en.wikipedia.org/wiki/Content_negotiation) article on Wikipedia.

* [Requests](#content-request-id)
* [Responses](#content-response-id)

### Requests {#content-request-id}

APIs MUST use `Accept-*` HTTP request headers to specify:
* Content type
* Language
* Encoding

````
curl -X 'GET' \
  'url /www.us-api.morningstar.com/enterprise-components/v1/securities/?securityId=FOUSA06N2B' \
    -H 'Accept: application/json' \
    -H 'Accept-Language: en-us' \ 
    -H 'Accept-Encoding: compress' \
    -H 'Authorization: Bearer {token-value}' \
...
````
#### Overriding Request Headers

You MUST use `Accept-*` HTTP request headers, but you MAY allow users to override the content type and/or the language/locale [(for localization)](#international-id) by using query parameters in the URI. In the following example, the value in the `langCult` parameter in the request URI overrides the value in the `Accept-Language` request header.

````
curl -X 'GET' \
  'url /www.us-api.morningstar.com/enterprise-components/v1/securities/?securityId=FOUSA06N2B&langCult=ca-FR' \
    -H 'Accept: application/json' \
    -H 'Accept-Language: en-us' \ 
    -H 'Accept-Encoding: compress' \
    -H 'Authorization: Bearer {token-value}' \
...
````

### Responses {content-#response-id}

API SHOULD return `application/json` in the `Content-Type` HTTP response header.

````
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 65
...
````
## Output Format {#output-id}

### Technical Standards

|Applies To|Standard|Example|
|:------|:-----|:-------|
|Output Schema| Default MUST be JSON.||
||Support for XML/CSV/Protobuf/JSONP is OPTIONAL unless mandated by client requirements.|
|Numbers|MUST be machine-readable and locale-neutral.||
||If JSON is used, numbers MUST be represented by JSON numbers, not JSON strings.|A number which is represented as `1,234,567.89` in the United States and `1.234.567,89` in France must be represented as `1234567.89`.|
|Strings|Where an API exposes strings that are populated by back-end systems instead of by API clients, the API MUST be responsible for translating these strings to the selected locale where available. This is to ensure consistency of translations across API clients as well as to ensure proper sorting and searching behaviour (where applicable).||
|Dates|MUST follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Times) and be expressed as an offset from UTC time.|Date = `2022-05-25`|
|||Combined date and time in UTC = `2014-05-25T16:45:49+00:00`|

## Logging and Tracing

Tracing requests through the full stack of an API is extremely useful for debugging and carrying out root cause analysis. Tracing allows operations teams to see each stage of a request as it passes through the API (backend services, data access, and so on). 

Tracing enables you to group all the information associated with a given request despite a distributed architecture.

Each request through the API should be given a unique identifier such as a GUID and which is persisted by each tier of the architecture in access logs, trace logging, and so on. Providing this identifier when reporting an issue shortens the time for resolution.

### Logging Standards
You MUST follow the [Application Logging Standard](https://mswiki.morningstar.com/display/technology/Application+Logging+Standard) that has been defined for software developed at Morningstar.

### Tracing Standards

* The API Gateway SHOULD be used to provide the initial request identifier.

* APIs SHOULD consider leveraging their framework or libraries request tracing functionality.

* If an API is not passed an `X-API-RequestId` header, it MUST generate a new UUID value to serve as its request ID. 

* The request ID MUST be included in:

  * All logs. 
  * The X-API-RequstID header in all HTTP requests the API makes.

* Responses MAY also include the request ID. 

* The request ID header value MUST have the following format:

```
X-API-RequestId: 06ea2732-08cc-4606-8085-f7514da34a03

```

## Caching

Caching refers to the storing of the output of a request and using it if the same request is made within a short timeframe. This can be done on the client, on the server, or in a middle layer such as a proxy server. 

### Communicating Caching Policy

* APIs MUST use appropriate HTTP `Cache-Control` headers to communicate caching policy, including if the API does not allow caching by clients. 

* APIs SHOULD use the following values to communicate that the response should not be cached/stored: `Cache-Control : no-cache` or  `Cache-Control : no-store`.

* APIs SHOULD use the following values to values to set cache duration: `Cache-Control : max-age={}` or `Cache-Control : s-maxage={}`
 
* APIs SHOULD use the `Vary` header to communicate which HTTP request headers affect the response and thus the cacheability of the response. 

    For example, if an API uses the `Accept` request header for content negotiation, the API should include the following value in the response: `Vary: Accept`


* APIs SHOULD use `ETags` or `If-Modified-Since` to allow clients to make conditional requests. 

### Communicating Caching Policy to Intermediate Web Caches 

* APIs SHOULD use HTTP `Cache-Control` headers to communicate caching policy to intermediate web caches (for example, Varnish) and CDNs (for example, Akamai). 

* APIs MAY communicate a different caching policy to an end client than to intermediate web caches and CDNs. 

* To require an intermediate web cache to have a different cache duration than the API cilent, the API SHOULD use the following value: `Cache-Control: s-maxage=`


* To allow intermediate web caches to cache the response but forbid API clients from caching the response, the API SHOULD send `Cache-Control` directives and the intermediate web caches SHOULD be programmed to accept `Cache-Control` headers from the API but send no-cache directives to clients. For example:

### Supporting HTTP 1

APIs MAY also set a corresponding `Expires` header to support HTTP 1.0 clients.

For example, if a request is made on May 27, 2021 14:32:00 GMT and the API would like it cached for 1 hour, the API would respond:

````
Cache-Control: max-age=3600</br>
Expires: Tue, 27 May 2014 15:32:00 GMT
````

To communicate that a response is not cacheable, an API SHOULD include the following headers in its response:

```
Cache-Control: no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: 0
```

### Cache Eviction

* APIs MUST consider whether and how they will perform automatic and manual cache eviction. For example, how will the API operations team respond if an API accidentally sends an incorrect response to clients? Note that if Cache-Control headers are sent to API clients, then it is impossible to invalidate all caches in all cases. 

* API clients MUST NOT add any additional caching that does not follow the caching policy communicated by the API. 

* However, API clients MAY implement a weaker policy than the one communicated by the API.
