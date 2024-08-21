# DOT Takeout

Dot Takeout is the ultimate tax reporting tool for the Polkadot ecosystem. By aggregating data across all Polkadot chains, Dot Takeout provides users with a comprehensive, automated report of all transactions and blocks where their addresses have appeared. Instead of manually tracking accounts accross different Polkadot parachains and on different indexers, Dot Takeout is a purpose built tool that provides you all the data for your accounts in one place. 

Whether you're an individual investor, a trader, or a business operating in the Polkadot ecosystem, Dot Takeout simplifies tax compliance, saving you time and ensuring accuracy in your tax filings, on all your favorite parachains.

<p align="center">
  <img width="773" alt="dottakeout" src="https://github.com/user-attachments/assets/ea82fd61-f8fc-4ada-9d37-79a9757cf69f">
</p>

# Get started

Find the application at https://dottakeout.xyz 

Note: the demo is limited to 2024/08/19 and 4 chains (Polkadot, Hydration, People & AssetHub) mainly for ease of deployment. 

# For developers

Get data & run the query

```bash
wget 
duckdb dottakeout.db 
```

Then run some queries

```sql 
SELECT number FROM polkadot WHERE json_extract(extrinsics, '$')::TEXT LIKE '%1Z6%';
```

# Team

- William Stevension
- Karim Jedda

Related: https://github.com/wsteves/polkadot-address-collector 

# License

MIT
