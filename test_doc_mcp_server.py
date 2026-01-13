# test_mcp.py
import pytest
from doc_mcp_server import search_diameter_pdf

def test_pdf_retrieval():
    # Test a known keyword in your Diameter.pdf
    query = "what does CCR stand for ?"
    result = search_diameter_pdf.fn(query)
    
    assert "Source: Page" in result
    assert len(result) > 0
    print("Test Passed: Context retrieved successfully.")
    print(result)

if __name__ == "__main__":
    test_pdf_retrieval()