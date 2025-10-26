namespace LDAPInjectionExample
{
    class Program
    {
        static void VulnerableMethod(string input)
        {
            DirectorySearcher searcher = new DirectorySearcher();
            searcher.Filter = "(&(objectCategory=person)(objectClass=user)(displayName=" + input + "))";
        }
    }
}

namespace DeprecatedCipherAlgorithmExample
{
    class Program
    {
        static void Main(string[] args)
        {
            // Usage of deprecated cipher algorithm (DES)
            DES des = DES.Create();
            Console.WriteLine("DES algorithm created.");
        }
    }
}

namespace DI.Services
{
    public class SqlInjectionService : ISqlInjectionService
    {
        public string UnionBased(string param)
        {
            string result = "";
            string query = "SELECT * from [dbo].[USER] WHERE NAME = '" + param + "';";

            try
            {
                using (SqlConnection connection = new SqlConnection(
                   GetConnectionString()))
                    {
                        connection.Open();

                        SqlCommand command = new SqlCommand(query, connection);
                        SqlDataReader reader = command.ExecuteReader();
                        while (reader.Read())
                        {
                            result += String.Format("Username: {0} Role: {1}", reader["NAME"], reader["ROLE"]);
                        }
                    }
            } catch(Exception e)
            {
                result = e.Message;
            }

            return result;
        }

        public string UnionBasedWithFormatString(string param)
        {
            string result = "";
            string query = String.Format("SELECT * from [dbo].[USER] WHERE NAME = '{0}';", param);

            try
            {
                using (SqlConnection connection = new SqlConnection(
                   GetConnectionString()))
                    {
                        connection.Open();

                        SqlCommand command = new SqlCommand(query, connection);
                        SqlDataReader reader = command.ExecuteReader();
                        while (reader.Read())
                        {
                            result += String.Format("Username: {0} Role: {1}", reader["NAME"], reader["ROLE"]);
                        }
                    }
            } catch(Exception e)
            {
                result = e.Message;
            }

            return result;
        }

        public string ErrorBasedWithFormatString(string param)
        {
            string result;
            string query = String.Format("INSERT INTO [dbo].[PRODUCT] (NAME) VALUES ('{0}');", param);

            try 
            {
                using (SqlConnection connection = new SqlConnection(
                   GetConnectionString()))
                    {
                        connection.Open();

                        SqlCommand command = new SqlCommand(query, connection);
                        SqlDataReader reader = command.ExecuteReader();
                        while (reader.Read())
                        {
                            System.Diagnostics.Debug.WriteLine(String.Format("{0}", reader[0]));
                        }
                    }

                result = "Product was added";

            } catch(Exception e)
            {
                result = e.Message;
            }

            return result;
        }
        #endregion
    }
}
