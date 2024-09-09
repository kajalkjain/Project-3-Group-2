function buildpatient() {
  // 加载本地JSON数据
  d3.json("/Users/igelchen/Desktop/js_method/data.json").then((data) => {
    
    // 假设data是从JSON文件获取的，这里我们不需要再手动定义数据
    // 你可以通过console.log(data)来检查JSON数据的格式
    console.log(data);

    const width = 600;
    const height = 400;
    const margin = { top: 20, right: 30, bottom: 50, left: 70 };

    // 创建SVG容器
    const svg = d3.select("#chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", `translate(${margin.left},${margin.top})`);

    // X轴：患者名字
    const x = d3.scaleBand()
      .domain(data.map(d => d.First_name))  // 使用患者的名字作为标签
      .range([0, width])
      .padding(0.1);

    // Y轴：账单金额
    const y = d3.scaleLinear()
      .domain([0, d3.max(data, d => d["Billing Amount"])])
      .nice()
      .range([height, 0]);

    // 创建柱状图
    svg.selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", d => x(d.First_name))
      .attr("y", d => y(d["Billing Amount"]))
      .attr("width", x.bandwidth())
      .attr("height", d => height - y(d["Billing Amount"]))
      .attr("fill", "steelblue");

    // 添加X轴
    svg.append("g")
      .attr("transform", `translate(0,${height})`)
      .call(d3.axisBottom(x))
      .selectAll("text")  // 旋转X轴的文字使其更易读
      .attr("transform", "rotate(-45)")
      .style("text-anchor", "end");

    // 添加Y轴
    svg.append("g")
      .call(d3.axisLeft(y));

    // 添加Y轴标签
    svg.append("text")
      .attr("text-anchor", "middle")
      .attr("transform", `translate(-50, ${height / 2}) rotate(-90)`)
      .text("Billing Amount (USD)");

    // 添加X轴标签
    svg.append("text")
      .attr("text-anchor", "middle")
      .attr("transform", `translate(${width / 2}, ${height + 40})`)
      .text("Patient Name");

  }).catch(error => {
    console.error('Error loading the JSON file:', error);
  });
}

// 调用函数
buildpatient();