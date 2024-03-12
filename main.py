from typing import Optional
from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore

project_id = "speedy-victory-336109"
location = "us" # Format is "us" or "eu"
processor_id = "f135c348cfac968e" # Create processor before running sample
# file_path = "WechatIMG551.png"
# mime_type = "image/png"
file_path = "001.pdf"
mime_type = "application/pdf"

def process_document_sample(
    project_id: str,
    location: str,
    processor_id: str,
    file_path: str,
    mime_type: str,
) -> None:
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=opts)
    name = client.processor_path(project_id, location, processor_id)

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Load binary data
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)

    # Configure the process request
    request = documentai.ProcessRequest(
        name=name,
        raw_document=raw_document,
    )

    result = client.process_document(request=request)
    document = result.document

    for page in document.pages:
        for barcode in page.detected_barcodes:
            print("Barcode: {}".format(barcode.barcode))
            print('---------------------------')
            

process_document_sample(project_id, location, processor_id,file_path, mime_type)