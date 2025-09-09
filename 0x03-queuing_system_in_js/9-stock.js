import express from "express";
import { createClient } from "redis";
import { promisify } from "util";

const listProducts = [
  {id: 1, name: 'Suitcase 250', price: 50, stock: 4},
  {id: 2, name: 'Suitcase 450', price: 100, stock: 10},
  {id: 3, name: 'Suitcase 650', price: 350, stock: 2},
  {id: 4, name: 'Suitcase 1050', price: 550, stock: 5},
];

const client = createClient();
const port = 1245;
const app = express();

client.on('error', (err) => {
  console.log(`Redis Client Error: ${err}`);
});

const setFunc = promisify(client.set).bind(client);
const getFunc = promisify(client.get).bind(client);

function getItemById(id) {
  return listProducts.find(obj => obj.id === parseInt(id));
}

function reserveStockById(itemId, stock) {
  return setFunc(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const reserved = await getFunc(`item.${itemId}`);
  return reserved ? parseInt(reserved): 0;
}

app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map(product => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvaialbleQuantity: product.stock
  }));
  return res.json(formattedProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;

  const product = getItemById(itemId);

  if (!product) {
    return res.json({"status": "Product not found"});
  }

  const reservedStock = await getCurrentReservedStockById(itemId);
  const currentQuantity = product.stock - reservedStock;

  const response = {
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: Math.max(0, currentQuantity)
  };

  return res.json(response);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(itemId);

  if (!product) {
    return res.json({"status": "Product not found"});
  }

  const currentReserved = await getCurrentReservedStockById(itemId);
  const availableStock = product.stock - currentReserved;

  if(availableStock < 1) {
    return res.json({"status": "Not enough stock available", "itemId": parseInt(itemId)})
  }
  
  await reserveStockById(itemId, currentReserved + 1);
  return res.json({"status": "Reservation confirmed", "itemId": parseInt(itemId)});
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
