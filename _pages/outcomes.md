---
layout: page
permalink: /outcomes/
title: Bombs
description: The list of bugs and vulnerabilities found during my research.
nav: true
nav_order: 4
---

<!-- pages/outcomes.md -->
<div class="outcomes">
<div class="container">
    <h2>Protocol Systems (12 CVEs)</h2>
    <h3>Live555 </h3>
    <div class="table-responsive">
    <table class="table table-sm table-borderless">
    <tr>
        <th scope="row"><font color="#B509AC">CVE-2021-38380 </th>
        <td> 
        Live555 through 1.08 mishandles huge requests for the same MP3 stream, leading to recursion and s stack-based buffer over-read. An attacker can leverage this to launch a DoS attack.
        </td>
        <th>CVSS severity score: 7.5</th>
    </tr>
    </table>
</div>
</div>

<div class="container">
    <h2>Database Management Systems (64 bugs)</h2>
    <h3>CockroachDB (17 bugs)</h3>
    <details>
    <summary>sql: support SCRUB on temp tables</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/83770">https://github.com/cockroachdb/cockroach/issues/83770</a> <br />
    </details>
    <details>
    <summary>Internal Error: Comparison Overload not Found</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/83792">https://github.com/cockroachdb/cockroach/issues/83792</a> <br />
    </details>
    <details>
    <summary>ERROR: no builtin aggregate for SUM_INT on [unknown]</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/83874">https://github.com/cockroachdb/cockroach/issues/83874</a> <br />
    </details>
    <details>
    <summary>Crashing by EXPLAIN Statement</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/83965">https://github.com/cockroachdb/cockroach/issues/83965</a> <br />
    </details>
    <details>
    <summary>Invalid Memory Address Error of Specific SQL Query</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/83973">https://github.com/cockroachdb/cockroach/issues/83973</a> <br />
    </details>
    <details>
    <summary>Unexpected Error of Unique Index</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/83976">https://github.com/cockroachdb/cockroach/issues/83976</a> <br />
    </details>
    <details>
    <summary>Crash: panic: RecordingStructured has 30 recordings; expected 1</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/84056">https://github.com/cockroachdb/cockroach/issues/84056</a> <br />
    </details>
    <details>
    <summary>Unexpected Overflow Error by Huge Interval Value</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/84154">https://github.com/cockroachdb/cockroach/issues/84154</a> <br />
    </details>
    <details>
    <summary>Inconsistent Case Return Types Decimal Int</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85356">https://github.com/cockroachdb/cockroach/issues/85356</a> <br />
    </details>
    <details>
    <summary>No Result Returned by SHOW COLUMN</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85388">https://github.com/cockroachdb/cockroach/issues/85388</a> <br />
    </details>
    <details>
    <summary>internal error: no volatility for cast decimal::timestamp</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85389">https://github.com/cockroachdb/cockroach/issues/85389</a> <br />
    </details>
    <details>
    <summary>opt: internal error: lookup for ComparisonExpr</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85390">https://github.com/cockroachdb/cockroach/issues/85390</a> <br />
    </details>
    <details>
    <summary>opt: internal error: no output column equivalent to 2</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85393">https://github.com/cockroachdb/cockroach/issues/85393</a> <br />
    </details>
    <details>
    <summary>Unexpected Error in SHOW COLUMNS</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85394">https://github.com/cockroachdb/cockroach/issues/85394</a> <br />
    </details>
    <details>
    <summary>opt: internal error: estimated row count must be non-zero </summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85499">https://github.com/cockroachdb/cockroach/issues/85499</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by UNION</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/85502">https://github.com/cockroachdb/cockroach/issues/85502</a> <br />
    </details>
    <details>
    <summary>An Unexpected Error in `CROSS MERGE JOIN`</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/cockroachdb/cockroach/issues/88104">https://github.com/cockroachdb/cockroach/issues/88104</a> <br />
    </details>
    <h3>DuckDB (1 bugs)</h3>
    <details>
    <summary>Crash When Creating Index</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/duckdb/duckdb/issues/4976">https://github.com/duckdb/duckdb/issues/4976</a> <br />
    </details>
    <h3>SQLite (28 bugs)</h3>
    <details>
    <summary>An Inconsistent Result Depending on Parenthesization</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/af3d07f908">https://sqlite.org/forum/forumpost/af3d07f908</a> <br />
    </details>
    <details>
    <summary>An Unexpected NULL Column Caused by Where Clause in RIGHT JOIN</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/41cc3851d8">https://sqlite.org/forum/forumpost/41cc3851d8</a> <br />
    </details>
    <details>
    <summary>Rows are Unexpectedly Filtered Out by DISTINCT in RIGHT JOIN</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/c06b10ad7e">https://sqlite.org/forum/forumpost/c06b10ad7e</a> <br />
    </details>
    <details>
    <summary>Expression or Constant in GroupBy Clause</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/2458c5dea2">https://sqlite.org/forum/forumpost/2458c5dea2</a> <br />
    </details>
    <details>
    <summary>Ambiguous Reference Error for Right Join</summary>
    Status: confirmed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/e90a8e6e6f">https://sqlite.org/forum/forumpost/e90a8e6e6f</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by WHERE when Joining Tables</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/687b0bf563">https://sqlite.org/forum/forumpost/687b0bf563</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by WHERE/RIGHT JOIN</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/5cfe08eed6">https://sqlite.org/forum/forumpost/5cfe08eed6</a> <br />
    </details>
    <details>
    <summary>Unexpected Result in Joining Virtual Tables</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/3902c7b833">https://sqlite.org/forum/forumpost/3902c7b833</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by Joining</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/c2554d560b">https://sqlite.org/forum/forumpost/c2554d560b</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by RIGHT JOIN on RTree Tables</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/087de2d9ec">https://sqlite.org/forum/forumpost/087de2d9ec</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by WHERE Again</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/de16c4abe2">https://sqlite.org/forum/forumpost/de16c4abe2</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by RIGHT JOIN</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/206d99a16d">https://sqlite.org/forum/forumpost/206d99a16d</a> <br />
    </details>
    <details>
    <summary>Unexpected Assertion Error in SQLite3MemCompare</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/800eecf5e6">https://sqlite.org/forum/forumpost/800eecf5e6</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by ORDER BY</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/323f86cc30">https://sqlite.org/forum/forumpost/323f86cc30</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by RIGHT JOIN with INDEX</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/c4676c4956">https://sqlite.org/forum/forumpost/c4676c4956</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by JSON</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/3d9caa45cb">https://sqlite.org/forum/forumpost/3d9caa45cb</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by Complicated JOINING</summary>
    Status: unconfirmed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/eeb8173cf8">https://sqlite.org/forum/forumpost/eeb8173cf8</a> <br />
    </details>
    <details>
    <summary>Assertion `pCur->eCurType==CURTYPE_VTAB' failed</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/dafe0500b0">https://sqlite.org/forum/forumpost/dafe0500b0</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by RIGHT JOIN Again</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/51e6959f61">https://sqlite.org/forum/forumpost/51e6959f61</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by Complicated JOINING Again</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/b40696f501">https://sqlite.org/forum/forumpost/b40696f501</a> <br />
    </details>
    <details>
    <summary>Unexpected Assertion Error in valueFromFunction</summary>
    Status: unconfirmed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/e3243e07e8">https://sqlite.org/forum/forumpost/e3243e07e8</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by FULL OUTER JOIN</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/5610c17c3d">https://sqlite.org/forum/forumpost/5610c17c3d</a> <br />
    </details>
    <details>
    <summary>Unexpected Expression on ON clause</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/57bdf2217d">https://sqlite.org/forum/forumpost/57bdf2217d</a> <br />
    </details>
    <details>
    <summary>Unexpected Expression Result by FULL OUTER JOIN</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/6650cd40b5">https://sqlite.org/forum/forumpost/6650cd40b5</a> <br />
    </details>
    <details>
    <summary>Unexpected Parse Error</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/1a7fea4651">https://sqlite.org/forum/forumpost/1a7fea4651</a> <br />
    </details>
    <details>
    <summary>Unexpected Assertion Error in whereRangeScanEst</summary>
    Status: fixed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/c3496cf6b1">https://sqlite.org/forum/forumpost/c3496cf6b1</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by Union</summary>
    Status: unconfirmed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/174afeae57">https://sqlite.org/forum/forumpost/174afeae57</a> <br />
    </details>
    <details>
    <summary>Assertion `pRec->nField>0 && pRec->nField<=pIdx->nSampleCol' failed.</summary>
    Status: unconfirmed<br />
    Link: <a href="https://sqlite.org/forum/forumpost/3607259d3c">https://sqlite.org/forum/forumpost/3607259d3c</a> <br />
    </details>
    <h3>TiDB (18 bugs)</h3>
    <details>
    <summary>incorrect unresolved column when using natural join</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/35522">https://github.com/pingcap/tidb/issues/35522</a> <br />
    </details>
    <details>
    <summary>unexpected unresolved column error when the view refers to dual table</summary>
    Status: fixed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/35527">https://github.com/pingcap/tidb/issues/35527</a> <br />
    </details>
    <details>
    <summary>Runtime error: invalid memory address</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/35623">https://github.com/pingcap/tidb/issues/35623</a> <br />
    </details>
    <details>
    <summary>Unexpected Result with a FALSE Expression in WHERE</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/35645">https://github.com/pingcap/tidb/issues/35645</a> <br />
    </details>
    <details>
    <summary>Unexpected Error by CAST and CHAR functions</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/35652">https://github.com/pingcap/tidb/issues/35652</a> <br />
    </details>
    <details>
    <summary>Unexpected Error for Function INET_ATON</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/35677">https://github.com/pingcap/tidb/issues/35677</a> <br />
    </details>
    <details>
    <summary>Unexpected Connection Lost</summary>
    Status: confirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/35678">https://github.com/pingcap/tidb/issues/35678</a> <br />
    </details>
    <details>
    <summary>Inconsistent Results in SELECT</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/36853">https://github.com/pingcap/tidb/issues/36853</a> <br />
    </details>
    <details>
    <summary>Unexpected Result by CONCAT_WS</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/36888">https://github.com/pingcap/tidb/issues/36888</a> <br />
    </details>
    <details>
    <summary>ERROR 8141 (HY000): assertion failed</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38295">https://github.com/pingcap/tidb/issues/38295</a> <br />
    </details>
    <details>
    <summary>Incorrect Results by `REGEXP`</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38303">https://github.com/pingcap/tidb/issues/38303</a> <br />
    </details>
    <details>
    <summary>Incorrect Result by `LEFT JOIN`</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38304">https://github.com/pingcap/tidb/issues/38304</a> <br />
    </details>
    <details>
    <summary>runtime error: invalid memory address or nil pointer dereference</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38305">https://github.com/pingcap/tidb/issues/38305</a> <br />
    </details>
    <details>
    <summary>Unexpected Results</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38310">https://github.com/pingcap/tidb/issues/38310</a> <br />
    </details>
    <details>
    <summary>Error [types:1690]%s value is out of range in '%s'</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38352">https://github.com/pingcap/tidb/issues/38352</a> <br />
    </details>
    <details>
    <summary>Unexpected Error: Failed to read auto-increment value from storage engine</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38483">https://github.com/pingcap/tidb/issues/38483</a> <br />
    </details>
    <details>
    <summary>Unexpected Results by RIGHT JOIN</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38654">https://github.com/pingcap/tidb/issues/38654</a> <br />
    </details>
    <details>
    <summary>rule PredicatePushDown pushes wrong filter across projection</summary>
    Status: unconfirmed<br />
    Link: <a href="https://github.com/pingcap/tidb/issues/38736">https://github.com/pingcap/tidb/issues/38736</a> <br />
    </details>
</div>

</div>