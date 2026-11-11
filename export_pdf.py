import asyncio
import nbformat
from nbconvert import WebPDFExporter

# повертаємо цикл подій, що вміє запускати підпроцеси (потрібно Playwright)
asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

nb = nbformat.read('Lab5/Lab5.ipynb', as_version=4)
pdf_bytes, _ = WebPDFExporter().from_notebook_node(nb)

with open('Lab5.pdf', 'wb') as f:
    f.write(pdf_bytes)
print('Готово: Lab5.pdf')