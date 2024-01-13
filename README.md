![Untitled Diagram drawio](https://github.com/gaoxiangmstrong/ai_english_project/assets/85563264/f5161cd4-a763-48a7-95c1-5eab0255bb67)# 创建新的repo，上传代码并书写文档
1. DB变更为sqlite。并用sqlalchemy.orm改写。理由：文档中表明大型项目用orm
2. 使用flask_jwt_extended 在登录成功后返回access_token 目的：前后端分离。
3. 一部分使用了传统服务器渲染的方式。理由：没有学过vue
4. 对vue目前的理解： 可以用js给标签添加data()和methods（）。作用：用js渲染数据以及添加事件
5. 画出大概的用户使用流程以及数据流动图


# 简单的user_flow
![Uploading <?xml version="1.0" encoding="UTF-8"?>
<!-- Do not edit this file with editors other than draw.io -->
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="1809px" height="590px" viewBox="-0.5 -0.5 1809 590" content="&lt;mxfile host=&quot;app.diagrams.net&quot; modified=&quot;2024-01-13T02:55:35.873Z&quot; agent=&quot;Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36&quot; etag=&quot;KDCgcQ4ANpi-7M15r2Bj&quot; version=&quot;22.1.18&quot; type=&quot;device&quot;&gt;&#10;  &lt;diagram id=&quot;3PiUt8Q_qmZYBz-4z717&quot; name=&quot;routes设计&quot;&gt;&#10;    &lt;mxGraphModel dx=&quot;1098&quot; dy=&quot;1012&quot; grid=&quot;1&quot; gridSize=&quot;10&quot; guides=&quot;1&quot; tooltips=&quot;1&quot; connect=&quot;1&quot; arrows=&quot;1&quot; fold=&quot;1&quot; page=&quot;1&quot; pageScale=&quot;1&quot; pageWidth=&quot;827&quot; pageHeight=&quot;1169&quot; math=&quot;0&quot; shadow=&quot;0&quot;&gt;&#10;      &lt;root&gt;&#10;        &lt;mxCell id=&quot;0&quot; /&gt;&#10;        &lt;mxCell id=&quot;1&quot; parent=&quot;0&quot; /&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-8&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;qgGEkMDl7oeKlFnBhog1-5&quot; target=&quot;b3d7eLiIVHc3scA0ARes-1&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;qgGEkMDl7oeKlFnBhog1-5&quot; value=&quot;start&quot; style=&quot;whiteSpace=wrap;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fontFamily=Verdana;fontSize=12;align=center;&quot; parent=&quot;1&quot; vertex=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;30&quot; y=&quot;340&quot; width=&quot;120&quot; height=&quot;50&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-9&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-1&quot; target=&quot;b3d7eLiIVHc3scA0ARes-4&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-1&quot; value=&quot;/tags&quot; style=&quot;whiteSpace=wrap;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fontFamily=Verdana;fontSize=12;align=center;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;220&quot; y=&quot;340&quot; width=&quot;120&quot; height=&quot;50&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-3&quot; value=&quot;选择用户感兴趣的标签&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;210&quot; y=&quot;400&quot; width=&quot;140&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-11&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-4&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;600&quot; y=&quot;365&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-4&quot; value=&quot;/questions&quot; style=&quot;whiteSpace=wrap;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fontFamily=Verdana;fontSize=12;align=center;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;413.5&quot; y=&quot;340&quot; width=&quot;120&quot; height=&quot;50&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-31&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;473.5&quot; y=&quot;430&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;474&quot; y=&quot;650&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-5&quot; value=&quot;设计测试用户英文能力的问题&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;383.5&quot; y=&quot;400&quot; width=&quot;180&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-14&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-6&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;770&quot; y=&quot;360&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-6&quot; value=&quot;db(news_reading)&quot; style=&quot;shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;610&quot; y=&quot;300&quot; width=&quot;100&quot; height=&quot;120&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-7&quot; value=&quot;获得数据库中的文章&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;605&quot; y=&quot;430&quot; width=&quot;130&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-16&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-12&quot; target=&quot;b3d7eLiIVHc3scA0ARes-15&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-12&quot; value=&quot;/&amp;amp;lt;user_name&amp;amp;gt;/reading/&amp;amp;lt;news_title&amp;amp;gt;&quot; style=&quot;whiteSpace=wrap;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fontFamily=Verdana;fontSize=12;align=center;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;790&quot; y=&quot;335&quot; width=&quot;260&quot; height=&quot;50&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-13&quot; value=&quot;用户开始阅读文章并可向ai提问&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;805&quot; y=&quot;400&quot; width=&quot;190&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-19&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0;entryY=0.5;entryDx=0;entryDy=0;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-15&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;1530&quot; y=&quot;360&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-15&quot; value=&quot;/&amp;amp;lt;user_name&amp;amp;gt;/reading/interactions&quot; style=&quot;whiteSpace=wrap;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fontFamily=Verdana;fontSize=12;align=center;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;1150&quot; y=&quot;332.5&quot; width=&quot;280&quot; height=&quot;55&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-17&quot; value=&quot;AI向用户提问确认用户理解&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;1205&quot; y=&quot;400&quot; width=&quot;170&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-27&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;entryPerimeter=0;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-20&quot; target=&quot;b3d7eLiIVHc3scA0ARes-24&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;1870&quot; y=&quot;740&quot; as=&quot;targetPoint&quot; /&gt;&#10;            &lt;Array as=&quot;points&quot;&gt;&#10;              &lt;mxPoint x=&quot;1830&quot; y=&quot;363&quot; /&gt;&#10;              &lt;mxPoint x=&quot;1830&quot; y=&quot;680&quot; /&gt;&#10;            &lt;/Array&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-28&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;entryPerimeter=0;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-20&quot; target=&quot;b3d7eLiIVHc3scA0ARes-6&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;1600&quot; y=&quot;170&quot; as=&quot;targetPoint&quot; /&gt;&#10;            &lt;Array as=&quot;points&quot;&gt;&#10;              &lt;mxPoint x=&quot;1660&quot; y=&quot;230&quot; /&gt;&#10;              &lt;mxPoint x=&quot;660&quot; y=&quot;230&quot; /&gt;&#10;            &lt;/Array&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-20&quot; value=&quot;/&amp;amp;lt;user_name&amp;amp;gt;/reading/summary&quot; style=&quot;whiteSpace=wrap;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fontFamily=Verdana;fontSize=12;align=center;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;1530&quot; y=&quot;335&quot; width=&quot;280&quot; height=&quot;55&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-23&quot; value=&quot;用户总结&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;1635&quot; y=&quot;410&quot; width=&quot;70&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-38&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-24&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;910&quot; y=&quot;390&quot; as=&quot;targetPoint&quot; /&gt;&#10;            &lt;Array as=&quot;points&quot;&gt;&#10;              &lt;mxPoint x=&quot;1200&quot; y=&quot;550&quot; /&gt;&#10;              &lt;mxPoint x=&quot;911&quot; y=&quot;550&quot; /&gt;&#10;            &lt;/Array&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-24&quot; value=&quot;db(story-vectors)&quot; style=&quot;shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;1150&quot; y=&quot;620&quot; width=&quot;100&quot; height=&quot;120&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-25&quot; value=&quot;保存文本以及向量化的数据&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;1115&quot; y=&quot;750&quot; width=&quot;170&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-29&quot; value=&quot;关联用户和文章&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;1070&quot; y=&quot;190&quot; width=&quot;110&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-30&quot; value=&quot;/user/&amp;amp;lt;username&amp;amp;gt;&quot; style=&quot;whiteSpace=wrap;html=1;rounded=0;shadow=0;comic=0;labelBackgroundColor=none;strokeWidth=1;fontFamily=Verdana;fontSize=12;align=center;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;414&quot; y=&quot;655&quot; width=&quot;120&quot; height=&quot;50&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-32&quot; value=&quot;用户主页&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;439&quot; y=&quot;720&quot; width=&quot;70&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-35&quot; style=&quot;edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;&quot; edge=&quot;1&quot; parent=&quot;1&quot; source=&quot;b3d7eLiIVHc3scA0ARes-30&quot;&gt;&#10;          &lt;mxGeometry relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;1140&quot; y=&quot;680&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;b3d7eLiIVHc3scA0ARes-39&quot; value=&quot;用户在向量化的数据库中匹配与阅读过的文章相似的文章&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;670&quot; y=&quot;705&quot; width=&quot;320&quot; height=&quot;30&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;      &lt;/root&gt;&#10;    &lt;/mxGraphModel&gt;&#10;  &lt;/diagram&gt;&#10;&lt;/mxfile&gt;&#10;"><defs/><g><path d="M 120 175 L 183.63 175" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 188.88 175 L 181.88 178.5 L 183.63 175 L 181.88 171.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="0" y="150" width="120" height="50" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 175px; margin-left: 1px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Verdana; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">start</div></div></div></foreignObject><text x="60" y="179" fill="rgb(0, 0, 0)" font-family="Verdana" font-size="12px" text-anchor="middle">start</text></switch></g><path d="M 310 175 L 377.13 175" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 382.38 175 L 375.38 178.5 L 377.13 175 L 375.38 171.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="190" y="150" width="120" height="50" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 175px; margin-left: 191px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Verdana; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">/tags</div></div></div></foreignObject><text x="250" y="179" fill="rgb(0, 0, 0)" font-family="Verdana" font-size="12px" text-anchor="middle">/tags</text></switch></g><rect x="180" y="210" width="140" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 225px; margin-left: 250px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">选择用户感兴趣的标签</div></div></div></foreignObject><text x="250" y="229" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">选择用户感兴趣的标签</text></switch></g><path d="M 503.5 175 L 536.8 175 L 563.63 175" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 568.88 175 L 561.88 178.5 L 563.63 175 L 561.88 171.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="383.5" y="150" width="120" height="50" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 175px; margin-left: 385px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Verdana; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">/questions</div></div></div></foreignObject><text x="444" y="179" fill="rgb(0, 0, 0)" font-family="Verdana" font-size="12px" text-anchor="middle">/questions</text></switch></g><path d="M 443.5 240 L 444 350.5 L 444 453.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 444 458.88 L 440.5 451.88 L 444 453.63 L 447.5 451.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="353.5" y="210" width="180" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 225px; margin-left: 444px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">设计测试用户英文能力的问题</div></div></div></foreignObject><text x="444" y="229" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">设计测试用户英文能力的问题</text></switch></g><path d="M 680 170 L 710 170 L 733.63 170" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 738.88 170 L 731.88 173.5 L 733.63 170 L 731.88 166.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 580 125 C 580 116.72 602.39 110 630 110 C 643.26 110 655.98 111.58 665.36 114.39 C 674.73 117.21 680 121.02 680 125 L 680 215 C 680 223.28 657.61 230 630 230 C 602.39 230 580 223.28 580 215 Z" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 680 125 C 680 133.28 657.61 140 630 140 C 602.39 140 580 133.28 580 125" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 183px; margin-left: 581px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">db(news_reading)</div></div></div></foreignObject><text x="630" y="186" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">db(news_reading)</text></switch></g><rect x="575" y="240" width="130" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 255px; margin-left: 640px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">获得数据库中的文章</div></div></div></foreignObject><text x="640" y="259" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">获得数据库中的文章</text></switch></g><path d="M 1020 170 L 1113.63 170" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 1118.88 170 L 1111.88 173.5 L 1113.63 170 L 1111.88 166.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="760" y="145" width="260" height="50" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 258px; height: 1px; padding-top: 170px; margin-left: 761px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Verdana; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">/&lt;user_name&gt;/reading/&lt;news_title&gt;</div></div></div></foreignObject><text x="890" y="174" fill="rgb(0, 0, 0)" font-family="Verdana" font-size="12px" text-anchor="middle">/&lt;user_name&gt;/reading/&lt;news_title&gt;</text></switch></g><rect x="775" y="210" width="190" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 225px; margin-left: 870px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">用户开始阅读文章并可向ai提问</div></div></div></foreignObject><text x="870" y="229" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">用户开始阅读文章并可向ai提问</text></switch></g><path d="M 1400 170 L 1450 170 L 1493.63 170" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 1498.88 170 L 1491.88 173.5 L 1493.63 170 L 1491.88 166.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="1120" y="142.5" width="280" height="55" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 278px; height: 1px; padding-top: 170px; margin-left: 1121px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Verdana; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">/&lt;user_name&gt;/reading/interactions</div></div></div></foreignObject><text x="1260" y="174" fill="rgb(0, 0, 0)" font-family="Verdana" font-size="12px" text-anchor="middle">/&lt;user_name&gt;/reading/interactions</text></switch></g><rect x="1175" y="210" width="170" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 225px; margin-left: 1260px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">AI向用户提问确认用户理解</div></div></div></foreignObject><text x="1260" y="229" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">AI向用户提问确认用户理解</text></switch></g><path d="M 1780 172.5 L 1800 172.5 L 1800 490 L 1226.37 490" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 1221.12 490 L 1228.12 486.5 L 1226.37 490 L 1228.12 493.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 1630 145 L 1630 40 L 630 40 L 630 103.63" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 630 108.88 L 626.5 101.88 L 630 103.63 L 633.5 101.88 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="1500" y="145" width="280" height="55" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 278px; height: 1px; padding-top: 173px; margin-left: 1501px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Verdana; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">/&lt;user_name&gt;/reading/summary</div></div></div></foreignObject><text x="1640" y="176" fill="rgb(0, 0, 0)" font-family="Verdana" font-size="12px" text-anchor="middle">/&lt;user_name&gt;/reading/summary</text></switch></g><rect x="1605" y="220" width="70" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 235px; margin-left: 1640px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">用户总结</div></div></div></foreignObject><text x="1640" y="239" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">用户总结</text></switch></g><path d="M 1170 430 L 1170 360 L 881 360 L 880.04 206.37" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 880.01 201.12 L 883.55 208.1 L 880.04 206.37 L 876.55 208.14 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 1120 445 C 1120 436.72 1142.39 430 1170 430 C 1183.26 430 1195.98 431.58 1205.36 434.39 C 1214.73 437.21 1220 441.02 1220 445 L 1220 535 C 1220 543.28 1197.61 550 1170 550 C 1142.39 550 1120 543.28 1120 535 Z" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><path d="M 1220 445 C 1220 453.28 1197.61 460 1170 460 C 1142.39 460 1120 453.28 1120 445" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 503px; margin-left: 1121px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">db(story-vectors)</div></div></div></foreignObject><text x="1170" y="506" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">db(story-vectors)</text></switch></g><rect x="1085" y="560" width="170" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 575px; margin-left: 1170px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">保存文本以及向量化的数据</div></div></div></foreignObject><text x="1170" y="579" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">保存文本以及向量化的数据</text></switch></g><rect x="1040" y="0" width="110" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 15px; margin-left: 1095px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">关联用户和文章</div></div></div></foreignObject><text x="1095" y="19" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">关联用户和文章</text></switch></g><rect x="384" y="465" width="120" height="50" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 118px; height: 1px; padding-top: 490px; margin-left: 385px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Verdana; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: normal; overflow-wrap: normal;">/user/&lt;username&gt;</div></div></div></foreignObject><text x="444" y="494" fill="rgb(0, 0, 0)" font-family="Verdana" font-size="12px" text-anchor="middle">/user/&lt;username&gt;</text></switch></g><rect x="409" y="530" width="70" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 545px; margin-left: 444px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">用户主页</div></div></div></foreignObject><text x="444" y="549" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">用户主页</text></switch></g><path d="M 504 490 L 807 490 L 1103.63 490" fill="none" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 1108.88 490 L 1101.88 493.5 L 1103.63 490 L 1101.88 486.5 Z" fill="rgb(0, 0, 0)" stroke="rgb(0, 0, 0)" stroke-miterlimit="10" pointer-events="all"/><rect x="640" y="515" width="320" height="30" fill="none" stroke="none" pointer-events="all"/><g transform="translate(-0.5 -0.5)"><switch><foreignObject pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility" style="overflow: visible; text-align: left;"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 1px; height: 1px; padding-top: 530px; margin-left: 800px;"><div data-drawio-colors="color: rgb(0, 0, 0); " style="box-sizing: border-box; font-size: 0px; text-align: center;"><div style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; pointer-events: all; white-space: nowrap;">用户在向量化的数据库中匹配与阅读过的文章相似的文章</div></div></div></foreignObject><text x="800" y="534" fill="rgb(0, 0, 0)" font-family="Helvetica" font-size="12px" text-anchor="middle">用户在向量化的数据库中匹配与阅读过的文章相似的文章</text></switch></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.drawio.com/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>Untitled Diagram.drawio.svg…]()
