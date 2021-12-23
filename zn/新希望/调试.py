import random
import time

seq = str(random.randint(10000,99999))
t = time.time()
tp = str(int(round(t * 1000)))
baseContAmount = random.randint(1,100)

zd = "{\"assetList\":[{\"acctName\":\"供应商的银行账户名\",\"acctNo\":\"供应商的银行账号\",\"bankName\":\"供应商的收款银行开户行\",\"baseContAmount\":10.0,\"baseContName\":\"基础交易合同名称\",\"baseContNo\":\"基础交易合同名称编号\",\"companyArea\":null,\"companyContracts\":\"闫学雷\",\"companyEmail\":null,\"companyName\":\"深圳市金兰湾贸易有限公司\",\"companyPhone\":\"13810957727\",\"companyVatNum\":\"91440300342921125A\",\"discountRate\":10.0,\"extendJson\":null,\"factorAmount\":100.0,\"fundNo\":\"NO1639477251\",\"fundType\":\"销售费用\",\"invoiceList\":[{\"invoiceAmount\":100.12,\"invoiceCode\":\"147703\",\"invoiceDistAmount\":1.11,\"invoiceNo\":\"95049212\",\"noTaxAmount\":1,\"verifyCode\":null}],\"limtedAmount\":1.0,\"merchCode\":null,\"requestNo\":\"RQ1639477251\",\"transferAmount\":10.0,\"vendorArea\":null,\"vendorContracts\":\"闫学雷\",\"vendorEmail\":null,\"vendorName\":\"中山市风行广告有限公司\",\"vendorPhone\":\"13810957727\",\"vendorVatNum\":\"914420007857977335\"}],\"merchCode\":null,\"seqNo\":\"seqNo%s\"}"%(seq)

rc = {
	"apiType": "ABS_ASSET_INFO",
	"appId": "dev_newhope",
	"dataStr": zd,
	"sign": "",
	"timestamp": tp
}
print(rc)