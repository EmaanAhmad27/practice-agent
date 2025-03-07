from crewai_tools import SerperDevTool, EXASearchTool, FileReadTool, FileWriterTool
research_tool = SerperDevTool()
SEO_tool = EXASearchTool(api_key="AIzaSyCY5pUyfadVdkFx2GBgAUq72rOlntlJyNk")
Writing_tool = FileReadTool()
Editor_tool = FileWriterTool()
