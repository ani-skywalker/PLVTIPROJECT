USE [PLVTIProject]
GO
/****** Object:  StoredProcedure [dbo].[customerSync]    Script Date: 12/15/2020 7:28:26 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		Arash&Avash
-- Create date: 1399-08-19
-- Description:	
-- =============================================
ALTER  PROCEDURE [dbo].[customerSync]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	set identity_insert [Customers] on 
	
	insert into [Customers]
	([id],[Name],[Family],[Address],[CSex],[CellPhone],[EcCode],[Email],[FAccId],[FPId],[FaxNo],[PhoneNo],[SCode],[TRes],[UserId],[ZipCode])
	SELECT [id]
      ,[Name]
      ,[Family]
      ,[Address]
      ,[CSex]
      ,[CellPhone]
      ,[EcCode]
      ,[Email]
      ,[FAccId]
      ,[FPId]
      ,[FaxNo]
      ,[PhoneNo]
      ,[SCode]
      ,[TRes]
      ,[UserId]
      ,[ZipCode]
  FROM [192.168.20.40].[goroohpakhsh].dbo.__Customer__
  where id not in (select id from [Customers])
  set identity_insert [Customers] off

  ---------------------------------------------

  delete from auth_user where customersid_id not in (select id  FROM [192.168.20.40].[goroohpakhsh].dbo.__Customer__) and customersid_id is not null and len(customersid_id)>0
  delete from [Customers] where id not in (select id  FROM [192.168.20.40].[goroohpakhsh].dbo.__Customer__)

  ---------------------------------------------


update b set 
	   b.[Name]      =a.[Name]
      ,b.[Family]	 =a.[Family]
      ,b.[Address]	 =a.[Address]
      ,b.[CSex]		 =a.[CSex]
      ,b.[CellPhone] =a.[CellPhone]
      ,b.[EcCode]	 =a.[EcCode]
      ,b.[Email]	 =a.[Email]
      ,b.[FAccId]	 =a.[FAccId]
      ,b.[FPId]		 =a.[FPId]
      ,b.[FaxNo]	 =a.[FaxNo]
      ,b.[PhoneNo]	 =a.[PhoneNo]
      ,b.[SCode]	 =a.[SCode]
      ,b.[TRes]		 =a.[TRes]
      ,b.[UserId]	 =a.[UserId]
      ,b.[ZipCode]	 =a.[ZipCode]
  FROM [192.168.20.40].[goroohpakhsh].dbo.__Customer__ a join Customers b on a.id=b.id

END
