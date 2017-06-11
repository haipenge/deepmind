package ${obj.component.get_test_package_name()}service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.commons.collections.CollectionUtils;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.util.Assert;

import ${obj.component.package_name()}.entity.${obj.name};
import com.faceye.feature.repository.jpa.SearchFilter;
import ${obj.component.package_name()}.service.${obj.name}Service;
import com.faceye.test.feature.service.BaseServiceTestCase;


/**
 * @说明:${obj.name}  服务层测试用例
 * 
 * @author @haipenge haipenge@gmail.com 
 * @Create Date:${obj.get_current_date()}
 */
public class ${obj.name}ServiceTestCase extends BaseServiceTestCase {
	@Autowired
	private ${obj.name}Service ${obj.get_lower_start_clazz_name()}Service = null;
	/**
	 * 初始化
	 * @todo
	 * @throws Exception
	 * @author:@haipenge
	 * haipenge@gmail.com
	 * 2014年5月20日
	 */
	@Before
	public void set() throws Exception {
		Assert.isTrue(${obj.name}Service != null);
	}

	/**
	 * 清理
	 * @todo
	 * @throws Exception
	 * @author:@haipenge
	 * haipenge@gmail.com
	 * 2014年5月20日
	 */
	@After
	public void after() throws Exception {
		this.${obj.get_lower_start_clazz_name()}Service.removeAllInBatch();
	}

	/**
	 *  保存测试
	 * @todo
	 * @throws Exception
	 * @author:@haipenge
	 * haipenge@gmail.com
	 * 2014年5月20日
	 */
	@Test
	public void testSave() throws Exception {
		${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
		this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		List<${obj.name}> entites = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isNotEmpty(entites));
	}

	@Test
	public void testSaveAndFlush() throws Exception {
		${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
		this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		List<${obj.name}> entites = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isNotEmpty(entites));
	}

	@Test
	public void testMultiSave() throws Exception {
		for (int i = 0; i < 5; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		}
		List<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isNotEmpty(entities) && entities.size() == 5);
	}

	@Test
	public void testRemoveById() throws Exception {
		${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
		this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		logger.debug(">>Entity id is:" + ${obj.get_lower_start_clazz_name()}.getId());
		${obj.name} e = this.${obj.get_lower_start_clazz_name()}Service.get(${obj.get_lower_start_clazz_name()}.getId());
		Assert.isTrue(e != null);
	}

	@Test
	public void testRemove${obj.name}() throws Exception {
		${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
		this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		this.${obj.get_lower_start_clazz_name()}Service.remove(${obj.get_lower_start_clazz_name()});
		List<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isEmpty(entities));
	}

	@Test
	public void testRemoveAllInBatch() throws Exception {
		for (int i = 0; i < 5; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		}
		List<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isNotEmpty(entities) && entities.size() == 5);
		this.${obj.get_lower_start_clazz_name()}Service.removeAllInBatch();
		entities = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isEmpty(entities));
	}

	@Test
	public void testRemoveAll() throws Exception {
		for (int i = 0; i < 5; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		}
		this.${obj.get_lower_start_clazz_name()}Service.removeAll();
		List<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isEmpty(entities));
	}

	@Test
	public void testRemoveListInBatch() throws Exception {
		List<${obj.name}> entities = new ArrayList<${obj.name}>();
		for (int i = 0; i < 5; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
			entities.add(${obj.get_lower_start_clazz_name()});
		}
		this.${obj.get_lower_start_clazz_name()}Service.removeInBatch(entities);
		entities = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isEmpty(entities));
	}

	@Test
	public void testGetAll() throws Exception {
		for (int i = 0; i < 5; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		}
		List<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Service.getAll();
		Assert.isTrue(CollectionUtils.isNotEmpty(entities) && entities.size() == 5);
	}

	@Test
	public void testGetPage() throws Exception {
		for (int i = 0; i < 25; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
		}
		Map<String, Object> searchParams = new HashMap<String, Object>();
		Page<${obj.name}> page = this.${obj.get_lower_start_clazz_name()}Service.getPage(searchParams, 1, 5);
		Assert.isTrue(page != null && page.getSize() == 5);
		searchParams.put("EQ_name", "test-10");
		page = this.${obj.get_lower_start_clazz_name()}Service.getPage(searchParams, 1, 5);
		Assert.isTrue(page != null && page.getTotalElements() == 1);
		searchParams = new HashMap<String, Object>();
		searchParams.put("LIKE_name", "test");
		page = this.${obj.get_lower_start_clazz_name()}Service.getPage(searchParams, 1, 5);

		Assert.isTrue(page != null && page.getTotalElements() == 25 && page.getNumberOfElements() == 5);

	}

	@Test
	public void testGet() throws Exception {
		Long id = null;
		for (int i = 0; i < 25; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
			id = ${obj.get_lower_start_clazz_name()}.getId();
		}
		${obj.name} e = this.${obj.get_lower_start_clazz_name()}Service.get(id);
		Assert.isTrue(e != null);
	}

	@Test
	public void testGetByIds() throws Exception {
		List<Long> ids = new ArrayList<Long>();
		for (int i = 0; i < 25; i++) {
			${obj.name} ${obj.get_lower_start_clazz_name()} = new ${obj.name}();
			this.${obj.get_lower_start_clazz_name()}Service.save(${obj.get_lower_start_clazz_name()});
			if (i < 5) {
				ids.add(${obj.get_lower_start_clazz_name()}.getId());
			}
		}
		List<${obj.name}> entities = this.${obj.get_lower_start_clazz_name()}Service.getAll(ids);
		Assert.isTrue(entities != null && entities.size() == 5);
	}
}
