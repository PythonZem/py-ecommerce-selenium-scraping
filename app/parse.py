import csv
import dataclasses
from dataclasses import dataclass
from urllib.parse import urljoin


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


BASE_URL = "https://webscraper.io/"

ENDPOINTS_URL = {
    "home": urljoin(BASE_URL, "test-sites/e-commerce/more/"),
    "computers": urljoin(BASE_URL, "/test-sites/e-commerce/more/computers/"),
    "laptops": urljoin(BASE_URL, "/test-sites/e-commerce/more/computers/laptops"),
    "tablets": urljoin(BASE_URL, "/test-sites/e-commerce/more/computers/tablets"),
    "phones": urljoin(BASE_URL, "/test-sites/e-commerce/more/phones"),
    "touch": urljoin(BASE_URL, "/test-sites/e-commerce/more/phones/touch")


}


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    num_of_reviews: int


PRODUCT_FIELDS = [filed.name for filed in dataclasses.fields(Product)]
driver = webdriver.Chrome()


def parse_single_product(product: WebElement):

    return Product(
        title=product.find_element(
            By.CLASS_NAME, "title"
        ).text,
        description=product.find_element(
            By.CLASS_NAME, "description"
        ).text,
        price=float(product.find_element(
            By.CLASS_NAME, "price"
        ).text.replace("$", "")),
        rating=len(
            product.find_elements(
                By.CLASS_NAME, "review-count"
            )
        ),
        num_of_reviews=int(
            product.find_element(
                By.CLASS_NAME, "review-count"
            ).text.split()[0]
        )
    )


def get_all_products() -> None:
    pass


def write_products_to_csv(filename: str, products: [Product]) -> None:
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(PRODUCT_FIELDS)
        writer.writerows([dataclasses.astuple(product) for product in products])


if __name__ == "__main__":
    get_all_products()
